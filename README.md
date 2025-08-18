# Elastic Scaling of Impala

<img width="600" height="488" alt="image" src="https://github.com/user-attachments/assets/740276af-d1a3-4eb7-8ca1-8a934d2978f3" />

An elastic computing architecture is rapidly becoming the standard for data-driven organizations that need to query massive datasets without maintaining a fleet of idle, expensive servers.
With the help of K8s, it provides the robust, scalable, and self-healing infrastructure needed to run a distributed SQL query engine. In this scalable Impala architecture, the autoscaler acts as a dedicated pod that monitors the Impala cluster's workload. When the coordinator pod receives the SQL query, parses it, creates an execution plan, and distributes tasks to the executor pods. Running each executor as a separate pod is what makes the system horizontally scalable.

## Here’s the workflow:

1. A user submits one or more complex SQL queries. Here's the sample of complex query.
2. The autoscaler observes metrics like the number of queued queries, CPU utilization on the existing executor pods, or memory pressure.

```
time="2025-08-15T04:49:32Z" level=info msg="needsScaleUp is true as there are 3 queries queued."
time="2025-08-15T04:49:32Z" level=info msg="Impala autoscaler will attempt to add executor group."
time="2025-08-15T04:49:32Z" level=info msg="Adding new executor group: impala-executor-001"
time="2025-08-15T04:49:32Z" level=info msg="Fetching history for release name: impala-executor-689eb14e-111b624b"
time="2025-08-15T04:49:32Z" level=info msg="Found historical release: impala-executor, Release Name: impala-executor-689eb14e-111b624b, Status: deployed, Version: 1"
time="2025-08-15T04:49:33Z" level=info msg="There is a scale up pending, targetExecutorGroups=2"
time="2025-08-15T04:49:33Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:49:53Z" level=info msg="Group Set: root.default Load: numQueriesQueued 3, numQueriesRunning 1"
time="2025-08-15T04:49:53Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:49:53Z" level=info msg="needsScaleDown/needsSuspend is false as scaling in progress, current executor groups=1, target =2"
time="2025-08-15T04:49:53Z" level=info msg="enoughConsecutive InScaleUp calls false as current 0 target 45"
time="2025-08-15T04:49:53Z" level=info msg="Scale up from 1 to 2 Executor Groups is in progress."
time="2025-08-15T04:49:53Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:50:13Z" level=info msg="CurrentExecutorGroups updated from 1 to 2"
time="2025-08-15T04:50:13Z" level=info msg="Group Set: root.default Load: numQueriesQueued 1, numQueriesRunning 2"
time="2025-08-15T04:50:13Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:50:13Z" level=info msg="needsScaleDown/needsSuspend is false as there are 1 queries queued."
time="2025-08-15T04:50:13Z" level=info msg="needsScaleUp is true as there are 1 queries queued."
time="2025-08-15T04:50:13Z" level=info msg="enoughConsecutive Up calls false as current 0 target 1"
time="2025-08-15T04:50:13Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:50:33Z" level=info msg="Group Set: root.default Load: numQueriesQueued 1, numQueriesRunning 2"
time="2025-08-15T04:50:33Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:50:33Z" level=info msg="needsScaleDown/needsSuspend is false as there are 1 queries queued."
time="2025-08-15T04:50:33Z" level=info msg="needsScaleUp is true as there are 1 queries queued."
time="2025-08-15T04:50:33Z" level=info msg="Impala autoscaler will attempt to add executor group."
time="2025-08-15T04:50:33Z" level=info msg="Adding new executor group: impala-executor-002"
time="2025-08-15T04:50:34Z" level=info msg="There is a scale up pending, targetExecutorGroups=3"
time="2025-08-15T04:50:34Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:50:55Z" level=info msg="Group Set: root.default Load: numQueriesQueued 1, numQueriesRunning 2"
time="2025-08-15T04:50:55Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:50:55Z" level=info msg="needsScaleDown/needsSuspend is false as scaling in progress, current executor groups=2, target =3"
time="2025-08-15T04:50:55Z" level=info msg="enoughConsecutive InScaleUp calls false as current 0 target 45"
time="2025-08-15T04:50:55Z" level=info msg="Scale up from 2 to 3 Executor Groups is in progress."
```
  
3. Sensing an increased load, it automatically communicates with the Kubernetes API to scale out, deploying new worker pods (executor-1, executor-2, and so on).

```
# kubectl -n impala-impala1 get pods
NAME                                 READY   STATUS            RESTARTS   AGE
catalogd-6987f8b6fb-8bvgw            2/2     Running           0          49m
coordinator-0                        4/4     Running           0          49m
hue-huedb-create-job-h6t4w           0/1     Completed         0          49m
huebackend-0                         2/2     Running           0          48m
huefrontend-57744b989-2s2rg          1/1     Running           0          48m
impala-autoscaler-5fbf84b757-dldp7   2/2     Running           0          49m
impala-executor-000-0                2/2     Running           0          49m
impala-executor-001-0                2/2     Running           0          115s
impala-executor-002-0                0/2     PodInitializing   0          54s
statestored-7db5c86b9c-hkzhd         2/2     Running           0          49m
```

Note that the CDW dashboard shows number of executor node has increased from 1 to 3 (indicated by the green bar).
<img width="800" height="293" alt="image" src="https://github.com/user-attachments/assets/90131568-1815-4816-976c-f7aac4d50451" />

4. These new pods seamlessly join the Impala cluster and immediately start processing tasks, speeding up query execution.
5. Once the workload subsides, the autoscaler will scale in, terminating the extra pods to save resources and reduce costs.

🚀 This elastic scaling ensures that you have exactly the right amount of compute power for your workload at any given moment, eliminating the classic problem of over-provisioning for peak loads or being under-provisioned and suffering from slow queries.







