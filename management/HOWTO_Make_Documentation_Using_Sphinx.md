## What do I need to do to created Sphinx documentation from my Python modules which contain documentation in GoogleStyle format?

To create Sphinx documentation from your Python modules which contain documentation in GoogleStyle format, you need to follow these general steps:

1. Install Sphinx and the sphinxcontrib-napoleon extension using pip:

```bash
pip install sphinx sphinxcontrib-napoleon
```

2. Create a Sphinx documentation project:

```bash
sphinx-quickstart
```

Follow the prompts to configure your project.

3. Add your Python module directory to the sys.path in the Sphinx conf.py file:

```python
import sys
sys.path.insert(0, '/path/to/your/module')
```

4. In the Sphinx conf.py file, configure the autodoc extension to generate documentation from your Python modules:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

autodoc_member_order = 'bysource'
```

5. Run the Sphinx apidoc command to generate a .rst file for your Python module:

```bash
sphinx-apidoc -o /path/to/docs/source /path/to/your/module
```

This will create a .rst file in your Sphinx source directory, which you can edit to include additional documentation and formatting.

6. Generate the Sphinx documentation by running:

```bash
sphinx-build -b html /path/to/docs/source /path/to/docs/build
```

This will create HTML documentation from your .rst files in the Sphinx build directory.

You can then open the index.html file in your web browser to view the documentation.

Note that these steps provide a basic outline for creating Sphinx documentation from Python modules with GoogleStyle documentation. Depending on your project's requirements, you may need to adjust the configuration or add additional steps to customize your documentation.

**./.**

