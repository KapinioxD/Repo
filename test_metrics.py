#!/usr/bin/env python3
# ai-generated: 100% - test script for DORA metrics validation
import json

# Load the fixture
with open('fixtures/metrics-practice.json', 'r') as f:
    fixture = json.load(f)

print("=== FIXTURE STRUCTURE ===")
print(json.dumps(fixture, indent=2))

# Verify all required fields exist and are not null
print("\n=== VALIDATION ===")

def check_field(obj, path, expected_type=None):
    parts = path.split('.')
    val = obj
    for part in parts:
        if isinstance(val, dict):
            val = val.get(part)
        else:
            print(f"❌ {path}: Not a dict at {part}")
            return False
    
    if val is None:
        print(f"❌ {path}: NULL value")
        return False
    elif expected_type and not isinstance(val, expected_type):
        print(f"❌ {path}: Expected {expected_type.__name__}, got {type(val).__name__}")
        return False
    else:
        print(f"✓ {path}: {type(val).__name__} = {val}")
        return True

# Check counts - all must be integers > 0 or 0
checks = [
    ('deployment_frequency_per_day', float),
    ('change_lead_time_seconds_p50', int),
    ('failed_deployment_recovery_time_seconds_p50', int),
    ('change_fail_rate', float),
    ('deployment_rework_rate', float),
    ('counts.deployments', int),
    ('counts.successful_deployments', int),
    ('counts.failed_deployments', int),
    ('counts.recovered_failures', int),
    ('counts.open_failures', int),
    ('counts.rework_deployments', int),
    ('counts.lead_time_pairs', int),
    ('counts.changes', int),
    ('anomalies.negative_lead_time_pairs', int),
    ('anomalies.deployments_without_commits', int),
    ('anomalies.commits_never_on_main', int),
    ('anomalies.revert_chains_collapsed', int),
    ('anomalies.overlapping_incident_pairs', int),
    ('ground_truth.changes_delivered', int),
    ('ground_truth.true_change_lead_time_seconds_p50', int),
]

for path, etype in checks:
    check_field(fixture, path, etype)
