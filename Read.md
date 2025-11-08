# Implementation of the deployment strategies

## Objective
Implement blue-green, rolling update, and canary strategies ensuring zero downtime while updating to latest image versions.


## Blue-Green
- Implementation:
  - Two Deployments: `mywebapp-blue` (v1) and `mywebapp-green` (v2).
  - Single Service `mywebapp-svc` whose selector is switched from `version: blue` to `version: green`.
- Zero downtime:
  - Green pod replicas are Ready (readiness probe) before switching.
  - Service selector change is atomic; traffic is switched to Ready pods instantly.

## Rolling Update
- Implementation:
  - Standard `Deployment` with `strategy.rollingUpdate` and `maxSurge: 1`, `maxUnavailable: 0`.
- Zero downtime:
  - `maxUnavailable: 0` ensures desired replicas remain available.
  - Kubernetes gradually replaces pods; readiness checks prevent directing traffic to unready pods.

## Canary (Argo Rollouts)
- Implementation:
  - `Rollout` resource with canary steps: `setWeight: 10 -> pause -> 50 -> pause -> 100`.
  - Uses pod-weight based canary where ratio of new and old pods are based on the weight set.
- Zero downtime:
  - Canary pods are created and become Ready before they receive significant traffic.
  - Final promotion replaces stable with canary when fully validated.



