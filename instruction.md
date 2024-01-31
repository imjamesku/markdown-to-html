Automating the compilation of markdown into directly embeddable HTML code, especially with math expressions, can be efficiently achieved using a combination of tools and scripts. Here's a process using Pandoc for markdown to HTML conversion and a scripting language like Python for automation. This setup also includes MathJax for math rendering in the final HTML.

### Tools You'll Need:

- **Pandoc**: A universal document converter that can convert markdown to HTML.
- **Python**: For automating the workflow. You'll create a script that watches for changes in your markdown files and automatically runs Pandoc to convert them to HTML.
- **MathJax**: For rendering math expressions in HTML. This can be included in your HTML template or added to the HTML output.

### Step-by-Step Guide:

1. **Install Pandoc**: First, ensure Pandoc is installed on your system. You can download it from [Pandoc's releases page](https://github.com/jgm/pandoc/releases) or install it through a package manager.

2. **Create a Python Script for Automation**:
   - Use a Python script to watch for changes in your markdown files and automatically compile them into HTML using Pandoc.
   - For file watching, you can use libraries like `watchdog`.

3. **Set Up MathJax**: Ensure your HTML template or output includes MathJax. You might use a custom Pandoc template with the MathJax script included or modify the HTML after conversion.

4. **Script Example**:
   Here's a basic Python script using `watchdog` and `subprocess` to watch a directory for markdown changes and compile them using Pandoc.

   ```python
   import time
   from watchdog.observers import Observer
   from watchdog.events import FileSystemEventHandler
   import subprocess

   class Watcher:
       DIRECTORY_TO_WATCH = "/path/to/your/markdown/files"

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

   class Handler(FileSystemEventHandler):
       @staticmethod
       def on_any_event(event):
           if event.is_directory:
               return None

           elif event.event_type == 'modified':
               # Take any action here when a file is modified.
               print(f"Markdown file changed: {event.src_path}")
               subprocess.run(["pandoc", event.src_path, "-s", "--mathjax", "-o", event.src_path.replace('.md', '.html')])

   if __name__ == "__main__":
       w = Watcher()
       w.run()
   ```

Replace `/path/to/your/markdown/files` with the path to your markdown files. This script watches for modifications in the specified directory and uses Pandoc to convert any changed markdown files into HTML, embedding MathJax for math expression rendering.

5. **Run the Script**: Execute the script to start watching for changes in your markdown files. Whenever you save changes to a file, the script automatically compiles it into HTML.

6. **Integrate Into Your Workflow**: Embed the generated HTML into your Teachable website or any other platform as needed.

This setup provides a highly flexible and automated workflow for converting markdown files into HTML, especially useful for educational content, technical documentation, or any scenario where markdown is preferred for content creation.