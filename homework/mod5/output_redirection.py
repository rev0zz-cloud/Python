import sys
import traceback


class Redirect:
    def __init__(self, stdout=sys.stdout, stderr=sys.stderr):
        self.old_out = sys.stdout
        self.stdout = stdout
        self.old_err = sys.stderr
        self.stderr = stderr

    def __enter__(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, type, value, traceback_false):
        sys.stdout = self.old_out
        if type is not None:
            sys.stderr.write(str(traceback.format_exc()))
        sys.stderr = self.old_err
        self.stdout.close()
        self.stderr.close()
        return True
