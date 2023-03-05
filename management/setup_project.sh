bash sudo apt install python3 python3-pip
bash sudo apt install git git-all
bash sudo apt install mkdocs
pip3 install --upgrade pip

# Data Prep Stack
# Environment
python3 -m venv environment
source ./environment/bin/activate

## Package Management
pip install pipx

## Excel
pip install xlrd
pip install xlwt
pip install xlutils
pip install pyxlsb
pip install openpyxl

## Database
pip install sqlalchemy

## Data Analysis
pip install numpy
pip install pandas==1.2

# Plotting
pip install matplotlib
pip install plotly
pip install seaborn
pip install bokeh
pip install altair
pip install cufflinks

# Processing
pip install parallel_pandas
pip install dask

## AWS
pip install aws-sso-util
pip install awsume
pip install boto3

# Documentation
pip install sphinx
## for GoogleStyle Python docs
pip install sphinxcontrib-napoleon

