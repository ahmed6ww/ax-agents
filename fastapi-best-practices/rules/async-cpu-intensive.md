---
title: Offload CPU-Intensive Tasks
impact: CRITICAL
impactDescription: Prevents server unresponsiveness
tags: async, cpu-bound, celery, multiprocessing
---

## Offload CPU-Intensive Tasks

Do not perform heavy CPU calculations (image processing, ML inference, heavy math) directly in FastAPI routes, whether `async` or `sync`.
- `async` routes will block the loop.
- `sync` routes run in threads, but the Python GIL prevents true parallelism for CPU tasks.

Offload these tasks to a separate process using `multiprocessing` or a task queue like Celery/RQ/Dramatiq.

**Incorrect (Heavy CPU work in route):**

```python
@router.post("/process-image")
def process(image: UploadFile):
    # Heavy CPU work blocks the thread and potentially other threads due to GIL
    result = heavy_image_processing(image) 
    return result
```

**Correct (Offloaded to task queue):**

```python
@router.post("/process-image")
def process(image: UploadFile, background_tasks: BackgroundTasks):
    # Offload to Celery or similar
    task_id = celery_app.send_task("process_image", args=[image.filename])
    return {"task_id": task_id}
```

Reference: [FastAPI Concurrency](https://fastapi.tiangolo.com/async/)
