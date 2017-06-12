# nameko-log-context
Data-driven log filter enabling logging custom fields from worker_ctx


Install
-------
```
pip install nameko-log-context
```

Using
-----

config.yml:

```yaml
...
log_context:
    root_call_id: 'lambda worker_ctx: worker_ctx._call_id_stack[0]'
    call_id: 'lambda worker_ctx: worker_ctx.call_id'
...

LOGGING:
    filters:
        log_context:
            (): nameko_log_context.LogFilter
    handlers:
        handler:
            filters:
                - log_context
    formatters:
        formatter:
            format: '...(root_call_id),(call_id)...'
```

Service:

```python
from nameko_log_context import LogContext
from nameko.rpc import rpc

class SomeService:
    log_context = LogContext()

    @rpc
    def method():
        """
        Every log message in this scope including logging in external
        packages is tagged with 'root_call_id' and 'call_id'
        """
```


How it works
------------

* Keys and lambda functions are retrieved on dependency provider setup
* Log tags are evaluated in worker_setup on each request and placed in thread-local object
* Log filter adds log tags from thread-local object to every log record