## pip install
Collecting fastmcp>=0.1.0 (from -r requirements.txt (line 2))
  Downloading fastmcp-3.3.1-py3-none-any.whl.metadata (8.2 kB)
Collecting playwright>=1.40.0 (from -r requirements.txt (line 3))
  Downloading playwright-1.60.0-py3-none-manylinux1_x86_64.whl.metadata (3.5 kB)
Collecting beautifulsoup4>=4.12.0 (from -r requirements.txt (line 4))
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting lxml>=4.9.0 (from -r requirements.txt (line 5))
  Downloading lxml-6.1.1-cp312-cp312-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (3.5 kB)
Collecting markitdown>=0.0.1 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading markitdown-0.1.5-py3-none-any.whl.metadata (4.1 kB)
Collecting fastmcp-slim==3.3.1 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading fastmcp_slim-3.3.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: platformdirs>=4.0.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (4.9.6)
Collecting pydantic-settings>=2.0.0 (from fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading pydantic_settings-2.14.1-py3-none-any.whl.metadata (3.4 kB)
Requirement already satisfied: pydantic>=2.11.7 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from pydantic[email]>=2.11.7->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (2.13.4)
Collecting python-dotenv>=1.1.0 (from fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
Collecting rich>=13.9.4 (from fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: typing-extensions>=4.0.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (4.15.0)
Collecting authlib>=1.6.11 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading authlib-1.7.2-py2.py3-none-any.whl.metadata (10 kB)
Collecting exceptiongroup>=1.2.2 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading exceptiongroup-1.3.1-py3-none-any.whl.metadata (6.7 kB)
Requirement already satisfied: httpx<1.0,>=0.28.1 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (0.28.1)
Collecting mcp<2.0,>=1.24.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading mcp-1.27.1-py3-none-any.whl.metadata (8.2 kB)
Collecting opentelemetry-api>=1.20.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading opentelemetry_api-1.42.1-py3-none-any.whl.metadata (1.4 kB)
Collecting py-key-value-aio<0.5.0,>=0.4.4 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading py_key_value_aio-0.4.4-py3-none-any.whl.metadata (15 kB)
Collecting cyclopts>=4.0.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading cyclopts-4.16.0-py3-none-any.whl.metadata (12 kB)
Collecting griffelib>=2.0.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading griffelib-2.0.2-py3-none-any.whl.metadata (1.3 kB)
Collecting jsonref>=1.1.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jsonref-1.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting jsonschema-path>=0.3.4 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jsonschema_path-0.5.0-py3-none-any.whl.metadata (8.1 kB)
Collecting openapi-pydantic>=0.5.1 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading openapi_pydantic-0.5.1-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: packaging>=24.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (26.2)
Collecting pyperclip>=1.9.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading pyperclip-1.11.0-py3-none-any.whl.metadata (2.4 kB)
Collecting python-multipart>=0.0.26 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading python_multipart-0.0.29-py3-none-any.whl.metadata (2.1 kB)
Requirement already satisfied: pyyaml<7.0,>=6.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (6.0.3)
Collecting uncalled-for>=0.2.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading uncalled_for-0.3.2-py3-none-any.whl.metadata (2.9 kB)
Collecting uvicorn>=0.35 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading uvicorn-0.48.0-py3-none-any.whl.metadata (6.7 kB)
Collecting watchfiles>=1.0.0 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading watchfiles-1.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
Collecting websockets>=15.0.1 (from fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading websockets-16.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)
Requirement already satisfied: anyio in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from httpx<1.0,>=0.28.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (4.13.0)
Requirement already satisfied: certifi in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from httpx<1.0,>=0.28.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (2026.5.20)
Requirement already satisfied: httpcore==1.* in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from httpx<1.0,>=0.28.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (1.0.9)
Requirement already satisfied: idna in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from httpx<1.0,>=0.28.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (3.16)
Requirement already satisfied: h11>=0.16 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from httpcore==1.*->httpx<1.0,>=0.28.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (0.16.0)
Collecting httpx-sse>=0.4 (from mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading httpx_sse-0.4.3-py3-none-any.whl.metadata (9.7 kB)
Collecting jsonschema>=4.20.0 (from mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting pyjwt>=2.10.1 (from pyjwt[crypto]>=2.10.1->mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading pyjwt-2.13.0-py3-none-any.whl.metadata (3.4 kB)
Collecting sse-starlette>=1.6.1 (from mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading sse_starlette-3.4.4-py3-none-any.whl.metadata (15 kB)
Collecting starlette>=0.27 (from mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading starlette-1.1.0-py3-none-any.whl.metadata (6.3 kB)
Requirement already satisfied: typing-inspection>=0.4.1 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (0.4.2)
Collecting beartype>=0.20.0 (from py-key-value-aio<0.5.0,>=0.4.4->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading beartype-0.22.9-py3-none-any.whl.metadata (37 kB)
Collecting aiofile>=3.5.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading aiofile-3.11.1-py3-none-any.whl.metadata (14 kB)
Collecting keyring>=25.6.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading keyring-25.7.0-py3-none-any.whl.metadata (21 kB)
Collecting cachetools>=5.0.0 (from py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading cachetools-7.1.4-py3-none-any.whl.metadata (5.5 kB)
Requirement already satisfied: annotated-types>=0.6.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from pydantic>=2.11.7->pydantic[email]>=2.11.7->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (0.7.0)
Requirement already satisfied: pydantic-core==2.46.4 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from pydantic>=2.11.7->pydantic[email]>=2.11.7->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (2.46.4)
Collecting pyee<14,>=13 (from playwright>=1.40.0->-r requirements.txt (line 3))
  Downloading pyee-13.0.1-py3-none-any.whl.metadata (3.0 kB)
Collecting greenlet<4.0.0,>=3.1.1 (from playwright>=1.40.0->-r requirements.txt (line 3))
  Downloading greenlet-3.5.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4>=4.12.0->-r requirements.txt (line 4))
  Downloading soupsieve-2.8.4-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: charset-normalizer in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (3.4.7)
Collecting defusedxml (from markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
Collecting magika~=0.6.1 (from markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading magika-0.6.3-py3-none-manylinux_2_28_x86_64.whl.metadata (10 kB)
Collecting markdownify (from markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading markdownify-1.2.2-py3-none-any.whl.metadata (9.9 kB)
Requirement already satisfied: requests in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (2.34.2)
Requirement already satisfied: click>=8.1.7 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from magika~=0.6.1->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (8.3.3)
Collecting onnxruntime>=1.17.0 (from magika~=0.6.1->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading onnxruntime-1.26.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting numpy>=1.26 (from magika~=0.6.1->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading numpy-2.4.6-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting caio~=0.9.0 (from aiofile>=3.5.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading caio-0.9.25-cp312-cp312-manylinux_2_34_x86_64.whl.metadata (3.3 kB)
Collecting cryptography (from authlib>=1.6.11->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading cryptography-48.0.0-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.3 kB)
Collecting joserfc>=1.6.0 (from authlib>=1.6.11->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading joserfc-1.6.7-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: attrs>=23.1.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from cyclopts>=4.0.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (26.1.0)
Collecting docstring-parser<4.0,>=0.15 (from cyclopts>=4.0.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading docstring_parser-0.18.0-py3-none-any.whl.metadata (3.5 kB)
Collecting rich-rst<3.0.0,>=1.3.1 (from cyclopts>=4.0.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading rich_rst-2.0.1-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: pygments>=2.0.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from rich-rst<3.0.0,>=1.3.1->cyclopts>=4.0.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2)) (2.20.0)
Collecting cffi>=2.0.0 (from cryptography->authlib>=1.6.11->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography->authlib>=1.6.11->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.20.0->mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=4.20.0->mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=4.20.0->mcp<2.0,>=1.24.0->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading rpds_py-0.30.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Collecting pathable<0.7.0,>=0.6.0 (from jsonschema-path>=0.3.4->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading pathable-0.6.0-py3-none-any.whl.metadata (7.2 kB)
Collecting SecretStorage>=3.2 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading secretstorage-3.5.0-py3-none-any.whl.metadata (4.0 kB)
Collecting jeepney>=0.4.2 (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jeepney-0.9.0-py3-none-any.whl.metadata (1.2 kB)
Collecting jaraco.classes (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting jaraco.functools (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jaraco_functools-4.5.0-py3-none-any.whl.metadata (2.9 kB)
Collecting jaraco.context (from keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading jaraco_context-6.1.2-py3-none-any.whl.metadata (4.2 kB)
Collecting azure-ai-documentintelligence (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading azure_ai_documentintelligence-1.0.2-py3-none-any.whl.metadata (53 kB)
Collecting azure-identity (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading azure_identity-1.25.3-py3-none-any.whl.metadata (91 kB)
Collecting mammoth~=1.11.0 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading mammoth-1.11.0-py2.py3-none-any.whl.metadata (26 kB)
Collecting olefile (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading olefile-0.47-py2.py3-none-any.whl.metadata (9.7 kB)
Collecting openpyxl (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading openpyxl-3.1.5-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting pandas (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pandas-3.0.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (79 kB)
Collecting pdfminer-six>=20251230 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pdfminer_six-20260107-py3-none-any.whl.metadata (4.3 kB)
Collecting pdfplumber>=0.11.9 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pdfplumber-0.11.9-py3-none-any.whl.metadata (43 kB)
Collecting pydub (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pydub-0.25.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting python-pptx (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading python_pptx-1.0.2-py3-none-any.whl.metadata (2.5 kB)
Collecting speechrecognition (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading speechrecognition-3.16.1-py3-none-any.whl.metadata (28 kB)
Collecting xlrd (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading xlrd-2.0.2-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting youtube-transcript-api~=1.0.0 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading youtube_transcript_api-1.0.3-py3-none-any.whl.metadata (23 kB)
Collecting cobble<0.2,>=0.1.3 (from mammoth~=1.11.0->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading cobble-0.1.4-py3-none-any.whl.metadata (2.7 kB)
Collecting flatbuffers (from onnxruntime>=1.17.0->magika~=0.6.1->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading flatbuffers-25.12.19-py2.py3-none-any.whl.metadata (1.0 kB)
Collecting protobuf (from onnxruntime>=1.17.0->magika~=0.6.1->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading protobuf-7.35.0-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)
Collecting pdfminer-six>=20251230 (from markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pdfminer_six-20251230-py3-none-any.whl.metadata (4.3 kB)
Collecting Pillow>=9.1 (from pdfplumber>=0.11.9->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pypdfium2>=4.18.0 (from pdfplumber>=0.11.9->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading pypdfium2-5.8.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (68 kB)
Collecting email-validator>=2.0.0 (from pydantic[email]>=2.11.7->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading email_validator-2.3.0-py3-none-any.whl.metadata (26 kB)
Collecting dnspython>=2.0.0 (from email-validator>=2.0.0->pydantic[email]>=2.11.7->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=13.9.4->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=13.9.4->fastmcp-slim==3.3.1->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: isodate>=0.6.1 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from azure-ai-documentintelligence->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (0.7.2)
Requirement already satisfied: azure-core>=1.30.0 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from azure-ai-documentintelligence->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (1.41.0)
Requirement already satisfied: urllib3<3,>=1.26 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from requests->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (2.7.0)
Collecting msal>=1.35.1 (from azure-identity->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading msal-1.36.0-py3-none-any.whl.metadata (11 kB)
Collecting msal-extensions>=1.2.0 (from azure-identity->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading msal_extensions-1.3.1-py3-none-any.whl.metadata (7.8 kB)
Collecting more-itertools (from jaraco.classes->keyring>=25.6.0->py-key-value-aio[filetree,keyring,memory]<0.5.0,>=0.4.4; extra == "client"->fastmcp-slim[client,server]==3.3.1->fastmcp>=0.1.0->-r requirements.txt (line 2))
  Downloading more_itertools-11.1.0-py3-none-any.whl.metadata (41 kB)
Requirement already satisfied: six<2,>=1.15 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from markdownify->markitdown>=0.0.1->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (1.17.0)
Collecting et-xmlfile (from openpyxl->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading et_xmlfile-2.0.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: python-dateutil>=2.8.2 in /root/.pyenv/versions/3.12.13/lib/python3.12/site-packages (from pandas->markitdown[all]>=0.0.1->-r requirements.txt (line 8)) (2.9.0.post0)
Collecting XlsxWriter>=0.5.7 (from python-pptx->markitdown[all]>=0.0.1->-r requirements.txt (line 8))
  Downloading xlsxwriter-3.2.9-py3-none-any.whl.metadata (2.7 kB)
Downloading fastmcp-3.3.1-py3-none-any.whl (7.9 kB)
Downloading fastmcp_slim-3.3.1-py3-none-any.whl (738 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 738.6/738.6 kB 21.4 MB/s  0:00:00
Downloading mcp-1.27.1-py3-none-any.whl (216 kB)
Downloading py_key_value_aio-0.4.4-py3-none-any.whl (152 kB)
Downloading playwright-1.60.0-py3-none-manylinux1_x86_64.whl (47.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.5/47.5 MB 39.1 MB/s  0:00:01
Downloading greenlet-3.5.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (611 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 611.4/611.4 kB 40.0 MB/s  0:00:00
Downloading pyee-13.0.1-py3-none-any.whl (15 kB)
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading lxml-6.1.1-cp312-cp312-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 33.0 MB/s  0:00:00
Downloading markitdown-0.1.5-py3-none-any.whl (63 kB)
Downloading magika-0.6.3-py3-none-manylinux_2_28_x86_64.whl (15.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.4/15.4 MB 32.9 MB/s  0:00:00
Downloading aiofile-3.11.1-py3-none-any.whl (20 kB)
Downloading caio-0.9.25-cp312-cp312-manylinux_2_34_x86_64.whl (80 kB)
Downloading authlib-1.7.2-py2.py3-none-any.whl (259 kB)
Downloading beartype-0.22.9-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 36.4 MB/s  0:00:00
Downloading cachetools-7.1.4-py3-none-any.whl (16 kB)
Downloading cyclopts-4.16.0-py3-none-any.whl (216 kB)
Downloading docstring_parser-0.18.0-py3-none-any.whl (22 kB)
Downloading rich_rst-2.0.1-py3-none-any.whl (272 kB)
Downloading exceptiongroup-1.3.1-py3-none-any.whl (16 kB)
Downloading griffelib-2.0.2-py3-none-any.whl (142 kB)
Downloading httpx_sse-0.4.3-py3-none-any.whl (9.0 kB)
Downloading joserfc-1.6.7-py3-none-any.whl (70 kB)
Downloading cryptography-48.0.0-cp311-abi3-manylinux_2_34_x86_64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 32.6 MB/s  0:00:00
Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
Downloading jsonref-1.1.0-py3-none-any.whl (9.4 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading jsonschema_path-0.5.0-py3-none-any.whl (24 kB)
Downloading pathable-0.6.0-py3-none-any.whl (18 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading keyring-25.7.0-py3-none-any.whl (39 kB)
Downloading jeepney-0.9.0-py3-none-any.whl (49 kB)
Downloading mammoth-1.11.0-py2.py3-none-any.whl (54 kB)
Downloading cobble-0.1.4-py3-none-any.whl (4.0 kB)
Downloading youtube_transcript_api-1.0.3-py3-none-any.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 24.7 MB/s  0:00:00
Downloading defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
Downloading numpy-2.4.6-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 36.6 MB/s  0:00:00
Downloading onnxruntime-1.26.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (18.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.2/18.2 MB 36.9 MB/s  0:00:00
Downloading openapi_pydantic-0.5.1-py3-none-any.whl (96 kB)
Downloading opentelemetry_api-1.42.1-py3-none-any.whl (61 kB)
Downloading pdfplumber-0.11.9-py3-none-any.whl (60 kB)
Downloading pdfminer_six-20251230-py3-none-any.whl (6.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.6/6.6 MB 7.3 MB/s  0:00:00
Downloading pillow-12.2.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 31.5 MB/s  0:00:00
Downloading pydantic_settings-2.14.1-py3-none-any.whl (60 kB)
Downloading email_validator-2.3.0-py3-none-any.whl (35 kB)
Downloading dnspython-2.8.0-py3-none-any.whl (331 kB)
Downloading pyjwt-2.13.0-py3-none-any.whl (31 kB)
Downloading pypdfium2-5.8.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.7/3.7 MB 32.6 MB/s  0:00:00
Downloading pyperclip-1.11.0-py3-none-any.whl (11 kB)
Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
Downloading python_multipart-0.0.29-py3-none-any.whl (29 kB)
Downloading rich-15.0.0-py3-none-any.whl (310 kB)
Downloading markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading rpds_py-0.30.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (394 kB)
Downloading secretstorage-3.5.0-py3-none-any.whl (15 kB)
Downloading soupsieve-2.8.4-py3-none-any.whl (37 kB)
Downloading sse_starlette-3.4.4-py3-none-any.whl (16 kB)
Downloading starlette-1.1.0-py3-none-any.whl (72 kB)
Downloading uncalled_for-0.3.2-py3-none-any.whl (11 kB)
Downloading uvicorn-0.48.0-py3-none-any.whl (71 kB)
Downloading watchfiles-1.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
Downloading websockets-16.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (184 kB)
Downloading azure_ai_documentintelligence-1.0.2-py3-none-any.whl (106 kB)
Downloading azure_identity-1.25.3-py3-none-any.whl (192 kB)
Downloading msal-1.36.0-py3-none-any.whl (121 kB)
Downloading msal_extensions-1.3.1-py3-none-any.whl (20 kB)
Downloading flatbuffers-25.12.19-py2.py3-none-any.whl (26 kB)
Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
Downloading jaraco_context-6.1.2-py3-none-any.whl (7.9 kB)
Downloading jaraco_functools-4.5.0-py3-none-any.whl (10 kB)
Downloading markdownify-1.2.2-py3-none-any.whl (15 kB)
Downloading more_itertools-11.1.0-py3-none-any.whl (72 kB)
Downloading olefile-0.47-py2.py3-none-any.whl (114 kB)
Downloading openpyxl-3.1.5-py2.py3-none-any.whl (250 kB)
Downloading et_xmlfile-2.0.0-py3-none-any.whl (18 kB)
Downloading pandas-3.0.3-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (10.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.9/10.9 MB 36.1 MB/s  0:00:00
Downloading protobuf-7.35.0-cp310-abi3-manylinux2014_x86_64.whl (327 kB)
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Downloading python_pptx-1.0.2-py3-none-any.whl (472 kB)
Downloading xlsxwriter-3.2.9-py3-none-any.whl (175 kB)
Downloading speechrecognition-3.16.1-py3-none-any.whl (32.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.9/32.9 MB 39.9 MB/s  0:00:00
Downloading xlrd-2.0.2-py2.py3-none-any.whl (96 kB)
Installing collected packages: pyperclip, pydub, flatbuffers, XlsxWriter, xlrd, websockets, uvicorn, uncalled-for, speechrecognition, soupsieve, rpds-py, python-multipart, python-dotenv, pypdfium2, pyjwt, pyee, pycparser, protobuf, Pillow, pathable, opentelemetry-api, olefile, numpy, more-itertools, mdurl, lxml, jsonref, jeepney, jaraco.context, httpx-sse, griffelib, greenlet, exceptiongroup, et-xmlfile, docstring-parser, dnspython, defusedxml, cobble, caio, cachetools, beartype, youtube-transcript-api, watchfiles, starlette, referencing, python-pptx, py-key-value-aio, playwright, pandas, openpyxl, onnxruntime, markdown-it-py, mammoth, jaraco.functools, jaraco.classes, email-validator, cffi, beautifulsoup4, aiofile, sse-starlette, rich, pydantic-settings, openapi-pydantic, markdownify, magika, jsonschema-specifications, jsonschema-path, cryptography, azure-ai-documentintelligence, SecretStorage, rich-rst, pdfminer-six, markitdown, jsonschema, joserfc, fastmcp-slim, pdfplumber, msal, mcp, keyring, cyclopts, authlib, msal-extensions, azure-identity, fastmcp

Successfully installed Pillow-12.2.0 SecretStorage-3.5.0 XlsxWriter-3.2.9 aiofile-3.11.1 authlib-1.7.2 azure-ai-documentintelligence-1.0.2 azure-identity-1.25.3 beartype-0.22.9 beautifulsoup4-4.14.3 cachetools-7.1.4 caio-0.9.25 cffi-2.0.0 cobble-0.1.4 cryptography-48.0.0 cyclopts-4.16.0 defusedxml-0.7.1 dnspython-2.8.0 docstring-parser-0.18.0 email-validator-2.3.0 et-xmlfile-2.0.0 exceptiongroup-1.3.1 fastmcp-3.3.1 fastmcp-slim-3.3.1 flatbuffers-25.12.19 greenlet-3.5.1 griffelib-2.0.2 httpx-sse-0.4.3 jaraco.classes-3.4.0 jaraco.context-6.1.2 jaraco.functools-4.5.0 jeepney-0.9.0 joserfc-1.6.7 jsonref-1.1.0 jsonschema-4.26.0 jsonschema-path-0.5.0 jsonschema-specifications-2025.9.1 keyring-25.7.0 lxml-6.1.1 magika-0.6.3 mammoth-1.11.0 markdown-it-py-4.2.0 markdownify-1.2.2 markitdown-0.1.5 mcp-1.27.1 mdurl-0.1.2 more-itertools-11.1.0 msal-1.36.0 msal-extensions-1.3.1 numpy-2.4.6 olefile-0.47 onnxruntime-1.26.0 openapi-pydantic-0.5.1 openpyxl-3.1.5 opentelemetry-api-1.42.1 pandas-3.0.3 pathable-0.6.0 pdfminer-six-20251230 pdfplumber-0.11.9 playwright-1.60.0 protobuf-7.35.0 py-key-value-aio-0.4.4 pycparser-3.0 pydantic-settings-2.14.1 pydub-0.25.1 pyee-13.0.1 pyjwt-2.13.0 pypdfium2-5.8.0 pyperclip-1.11.0 python-dotenv-1.2.2 python-multipart-0.0.29 python-pptx-1.0.2 referencing-0.37.0 rich-15.0.0 rich-rst-2.0.1 rpds-py-0.30.0 soupsieve-2.8.4 speechrecognition-3.16.1 sse-starlette-3.4.4 starlette-1.1.0 uncalled-for-0.3.2 uvicorn-0.48.0 watchfiles-1.2.0 websockets-16.0 xlrd-2.0.2 youtube-transcript-api-1.0.3
## check_env

[0;34m========================================[0m
[0;34m  环境检查 - qiaomu-anything-to-notebooklm[0m
[0;34m========================================[0m

[1;33m[1/8] Python 版本[0m
[0;32m✅ Python 3.12.13[0m

[1;33m[2/9] 核心 Python 依赖[0m
[0;32m✅ fastmcp 已安装[0m
[0;32m✅ playwright 已安装[0m
[0;32m✅ beautifulsoup4 已安装[0m
[0;32m✅ lxml 已安装[0m
[0;32m✅ markitdown 已安装[0m

[1;33m[3/9] Playwright 可导入性[0m
[0;32m✅ Playwright 可以正常导入[0m

[1;33m[4/9] NotebookLM CLI[0m
[0;31m❌ notebooklm 未找到[0m

[1;33m[5/9] markitdown CLI[0m
[0;32m✅ markitdown 已安装 (markitdown 0.1.5)[0m

[1;33m[6/9] Git 命令[0m
[0;32m✅ git 已安装 (git version 2.43.0)[0m

[1;33m[7/9] MCP 服务器文件[0m
[0;31m❌ MCP 服务器文件不存在: /workspace/research/qiaomu-anything-to-notebooklm-src/wexin-read-mcp/src/server.py[0m

[1;33m[8/9] MCP 配置[0m
[0;31m❌ 未找到 Claude 配置文件: /root/.claude/config.json[0m

[1;33m[9/9] NotebookLM 认证[0m
[0;31m❌ NotebookLM 认证检查失败: [Errno 2] No such file or directory: 'notebooklm'[0m

[0;34m========================================[0m
[0;31m❌ 检查失败 (9/13)，请运行 install.sh 重新安装。[0m
[0;34m========================================[0m

💡 修复建议：
  1. 运行安装脚本：./install.sh
  2. 配置 MCP：编辑 ~/.claude/config.json
  3. 认证 NotebookLM：notebooklm login

## run local markdown
📋 检测到输入类型: document
📄 处理文档: sample_public_domain.md
## run public url
📋 检测到输入类型: url
🌐 处理 URL: https://example.com
## run invalid path
📋 检测到输入类型: search
## baseline manual workflow

## baseline fallback note
网络访问受限，改用本地样例手工清洗流程。
