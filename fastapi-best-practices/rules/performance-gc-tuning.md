---
title: Garbage Collection Tuning
impact: MEDIUM
impactDescription: Reduces latency spikes in high-load apps
tags: performance, gc, memory
---

## Garbage Collection (GC) Tuning

For high-performance, high-throughput applications, Python's default GC behavior can cause latency spikes. Tuning GC thresholds can help.

**Example Tuning:**

```python
import gc

# Run at startup
def tune_gc():
    gc.collect(2) # Full collection
    gc.freeze() # Freeze startup objects to permanent generation
    gc.set_threshold(50_000, 10, 10) # Increase young gen threshold
```

Reference: [Instagram Engineering: Dismissing Python Garbage Collection at Instagram](https://instagram-engineering.com/dismissing-python-garbage-collection-at-instagram-4dca40b29172)
