import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/jamesku/repos/projects/markdown-to-html/markdown"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

def prepend_mathjax_script(html_file):
    mathjax_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS_HTML"></script>\n'
    with open(html_file, 'r') as file:
        html_content = file.read()

    html_content = mathjax_script + html_content

    with open(html_file, 'w') as file:
        file.write(html_content)

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified' and event.src_path.endswith('.md'):
            # Take any action here when a file is modified.
            print(f"Markdown file changed: {event.src_path}")
            output_html = event.src_path.replace('.md', '.html')
            subprocess.run(["pandoc", event.src_path, "-t", "html", '--mathjax', "-o", output_html])

            # Insert MathJax script into the generated HTML
            prepend_mathjax_script(output_html)


if __name__ == "__main__":
    w = Watcher()
    w.run()
