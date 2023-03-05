## How do I need to call sphinx-quickstart to create the basis for documentation in markdown?

To create the basis for documentation in markdown using sphinx-quickstart, you can follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you want to create your Sphinx documentation.

2. Run the sphinx-quickstart command to start the quickstart process:

```bash
sphinx-quickstart
```

3. You will be prompted to answer a series of questions to configure your Sphinx project. Here are some recommended settings for creating documentation in markdown:
	1. Separate source and build directories (y/n) - Answer y to create separate directories for your source files and generated documentation.
	2. Name prefix for templates and static dir - Leave this blank to use the default value.
	3. Project name - Enter the name of your project.
	4. Author name(s) - Enter your name and any other authors.
	5. Project release [] - Leave this blank for now.
	6. Project language [en] - Enter the language of your documentation, if different from English.
	7. Source file suffix [.rst] - Change this to .md to use markdown files for your source files.
	8. Name of your master document (without suffix) - Change this to index to use a markdown file named index.md as your main documentation file.
	9. Do you want to use the epub builder (y/n) - Answer n if you don't need to generate epub files.
	10. autodoc: automatically insert docstrings from modules (y/n) - Answer n if you don't need to generate documentation from your code.
	11. Do you want to document a project with multiple versions (y/n) - Answer n for now.
	12. Do you want to configure setup.py with your project's information (y/n) - Answer n for now.
4. Once you have answered all the questions, Sphinx will generate a set of files and directories for your documentation, including a conf.py file and a index.md file in the source directory.
5. Edit the conf.py file as necessary to configure your Sphinx project, including setting the extensions list and other settings specific to your documentation.
6. Edit the index.md file and other markdown files as necessary to create your documentation.
7. To generate HTML documentation from your markdown files, run the following command in your terminal or command prompt:

```bash
sphinx-build -b html sourcedir builddir
```

Replace sourcedir with the path to your source directory (usually named source), and builddir with the path to your build directory (usually named build).
8. This will generate HTML documentation from your markdown files and place the output files in the build directory. You can view the generated documentation by opening the index.html file in your web browser.

**./.**

