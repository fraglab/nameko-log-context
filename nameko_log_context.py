from threading import local
from logging import Filter

from nameko.extensions import DependencyProvider


class LogContext(DependencyProvider):
    thread_local = local()

    def __init__(self):
        super().__init__()
        self.log_keys = None

    def setup(self):
        config = self.container.config['log_context']
        self.log_keys = {k: eval(expr) for k, expr in config.items()}

    def worker_setup(self, worker_ctx):
        for k, func in self.log_keys.items():
            setattr(LogContext.thread_local, k, func(worker_ctx))


class LogFilter(Filter):
    def filter(self, record):
        for k, v in vars(LogContext.thread_local).items():
            setattr(record, k, v)
        return True
