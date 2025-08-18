import jaydebeapi
import os
os.environ['JAVA_HOME'] = '/opt/homebrew/opt/openjdk'
impala_driver_jar = "/Users/dennislee/workspace/ImpalaJDBC42-2.6.33.1062.jar"
jdbc_url = "jdbc:impala://coordinator-impala1.apps.dlee5.cldr.example:443/default;AuthMech=3;transportMode=http;httpPath=cliservice;ssl=1;AllowSelfSignedCerts=1"
credentials = ["dennislee", "PASSWORD"]

complex_query = """
SELECT
    t1.id AS id_1,
    t2.id AS id_2,
    t3.id AS id_3,
    t1.manufacturer,
    t2.event_type,
    -- Calculate a pseudo-distance between two points
    SQRT(POWER(t1.longitude - t2.longitude, 2) + POWER(t1.latitude - t2.latitude, 2)) AS distance,
    -- A complex aggregation to force more computation
    AVG(t1.iot_signal_1 + t2.iot_signal_3 + t3.iot_signal_4) AS combined_signal_avg,
    -- Use a hash function in the final output to add another layer of processing
    -- Note: Impala does not have a built-in MD5 function. You might need to use a UDF
    -- or replace this with another string function like `fnv_hash`.
    -- For this example, we will comment it out or replace it if an alternative is available.
    -- MD5(CONCAT(t1.device_id, t2.manufacturer, t3.event_type)) AS composite_hash
    CONCAT(t1.device_id, t2.manufacturer, t3.event_type) AS composite_key
FROM
    db1.celltowers t1
-- Use CROSS JOIN to create a massive number of row combinations to process.
CROSS JOIN
    db1.celltowers t2
CROSS JOIN
    db1.celltowers t3
WHERE
    -- Ensure we are not joining a row with itself, but in a slightly complex way.
    t1.id <> t2.id AND t2.id <> t3.id AND t1.id <> t3.id
    -- An expensive geospatial-like calculation to filter rows based on proximity.
    AND SQRT(POWER(t1.longitude - t3.longitude, 2) + POWER(t1.latitude - t3.latitude, 2)) < (
        -- Correlated subquery: This runs for each row of the outer query, making it very slow.
        SELECT AVG(t4.iot_signal_1) * 0.1 FROM db1.celltowers t4 WHERE t4.manufacturer = t1.manufacturer
    )
    -- Use mathematical functions that need to be computed for each row comparison.
    AND POWER(t1.iot_signal_1, 2) + POWER(t2.iot_signal_3, 2) > 5000
    -- Use LIKE with a leading wildcard, which prevents the engine from using an index efficiently.
    AND t2.manufacturer LIKE '%Connect%'
    AND t1.cell_tower_failure = 1
GROUP BY
    t1.id,
    t2.id,
    t3.id,
    t1.manufacturer,
    t2.manufacturer, -- Added to fix the error
    t2.event_type,
    t3.event_type,   -- Added to fix the error
    t1.device_id,
    t1.longitude,
    t1.latitude,
    t2.longitude,
    t2.latitude
HAVING
    -- Filter the grouped results based on an aggregate function.
    COUNT(*) > 0 AND AVG(t3.iot_signal_4) > 100
ORDER BY
    -- Order the results by a computationally expensive function.
    combined_signal_avg DESC,
    composite_key ASC
-- Finally, limit the output after all the heavy processing is done.
LIMIT 100
"""

conn = None
try:
    # Establish the connection
    print("Attempting to connect to Impala...")
    conn = jaydebeapi.connect(
        "com.cloudera.impala.jdbc.Driver", # The main driver class name
        jdbc_url,
        credentials,
        impala_driver_jar
    )
    print("Successfully connected to Impala.")

    print("\nExecuting complex query... this may take some time.")
    curs = conn.cursor()
    curs.execute(complex_query)
    print("Query execution finished.")

    results = curs.fetchall()

    if results:
        print("\nQuery Results:")
        print("--------------")
        # Get column names from the cursor description for a header
        column_names = [desc[0] for desc in curs.description]
        print(" | ".join(column_names))
        print("-" * (len(" | ".join(column_names)))) # Dynamic separator line

        # Print each row, converting all items to strings for display
        for row in results:
            print(" | ".join(str(item) for item in row))
        print("--------------")
        print(f"\nFetched {len(results)} rows.")
    else:
        print("Query executed successfully, but returned no results.")


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
        print("Connection closed.")
