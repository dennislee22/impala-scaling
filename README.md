# Scaling Impala



```
time="2025-08-15T04:49:12Z" level=info msg="needsSuspend is false because DisableAutoSuspend is true."
time="2025-08-15T04:49:12Z" level=info msg="needsScaleUp is true as there are 3 queries queued."
time="2025-08-15T04:49:12Z" level=info msg="enoughConsecutive Up calls false as current 0 target 1"
time="2025-08-15T04:49:12Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:49:32Z" level=info msg="Group Set: root.default Load: numQueriesQueued 3, numQueriesRunning 1"
time="2025-08-15T04:49:32Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:49:32Z" level=info msg="needsScaleDown is false as current Executor Groups 1 is at or below a minimum number of executor groups 1, maximum is 3."
time="2025-08-15T04:49:32Z" level=info msg="needsSuspend is false because DisableAutoSuspend is true."
time="2025-08-15T04:49:32Z" level=info msg="needsScaleUp is true as there are 3 queries queued."
time="2025-08-15T04:49:32Z" level=info msg="Impala autoscaler will attempt to add executor group."
time="2025-08-15T04:49:32Z" level=info msg="Adding new executor group: impala-executor-001"
time="2025-08-15T04:49:32Z" level=warning msg="No current healthy release found for service name: impala-executor"
time="2025-08-15T04:49:32Z" level=info msg="Fetching history for release name: impala-executor-689eb14e-111b624b"
time="2025-08-15T04:49:32Z" level=info msg="Found historical release: impala-executor, Release Name: impala-executor-689eb14e-111b624b, Status: deployed, Version: 1"
time="2025-08-15T04:49:32Z" level=info msg="Installing executor group \"impala-executor-001\" in namespace \"impala-impala1\""
W0815 04:49:33.142196       1 warnings.go:70] unknown field "spec.template.spec.securityContext.capabilities"
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
time="2025-08-15T04:50:34Z" level=warning msg="No current healthy release found for service name: impala-executor"
time="2025-08-15T04:50:34Z" level=info msg="Fetching history for release name: impala-executor-689eb14e-111b624b"
time="2025-08-15T04:50:34Z" level=info msg="Fetching history for release name: impala-executor-689ebc5c-12199cd9"
time="2025-08-15T04:50:34Z" level=info msg="Found historical release: impala-executor, Release Name: impala-executor-689ebc5c-12199cd9, Status: deployed, Version: 1"
time="2025-08-15T04:50:34Z" level=info msg="Found historical release: impala-executor, Release Name: impala-executor-689eb14e-111b624b, Status: deployed, Version: 1"
time="2025-08-15T04:50:34Z" level=info msg="Installing executor group \"impala-executor-002\" in namespace \"impala-impala1\""
W0815 04:50:34.755629       1 warnings.go:70] unknown field "spec.template.spec.securityContext.capabilities"
time="2025-08-15T04:50:34Z" level=info msg="There is a scale up pending, targetExecutorGroups=3"
time="2025-08-15T04:50:34Z" level=info msg="Impala-autoscaler sleeping for 20s"
time="2025-08-15T04:50:55Z" level=info msg="Group Set: root.default Load: numQueriesQueued 1, numQueriesRunning 2"
time="2025-08-15T04:50:55Z" level=info msg="Processing Group Set: root.default"
time="2025-08-15T04:50:55Z" level=info msg="needsScaleDown/needsSuspend is false as scaling in progress, current executor groups=2, target =3"
time="2025-08-15T04:50:55Z" level=info msg="enoughConsecutive InScaleUp calls false as current 0 target 45"
time="2025-08-15T04:50:55Z" level=info msg="Scale up from 2 to 3 Executor Groups is in progress."
```

<img width="1185" height="293" alt="image" src="https://github.com/user-attachments/assets/90131568-1815-4816-976c-f7aac4d50451" />


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

