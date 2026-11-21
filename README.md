# ✦ Insight Vision AI — Next-Generation Local AI

A comprehensive **AI-powered multimodal analysis platform** built with **Python, Streamlit, Ollama, and advanced vision-language models**.

Analyze images, interrogate documents, compare visuals, generate code, and extract structured data — all running **100% locally** on your machine with complete privacy.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Key Features](#-key-features)
* [New Features](#-new-features)
* [Technologies Used](#-technologies-used)
* [System Requirements](#-system-requirements)
* [Prerequisites](#-prerequisites)
* [Installation](#-installation)
* [Ollama Setup](#-ollama-setup)
* [Running the Application](#-running-the-application)
* [Complete Feature List](#-complete-feature-list)
* [Usage Guide](#-usage-guide)
* [Example Use Cases](#-example-use-cases)
* [Troubleshooting](#-troubleshooting)
* [Performance](#-performance)
* [Security and Privacy](#-security-and-privacy)
* [Future Enhancements](#-future-enhancements)
* [License](#-license)

---

# 📖 Overview

**Insight Vision AI** is a professional-grade, local-first AI application that combines:

* **Streamlit** — Modern web interface
* **Python** — Application logic and data processing
* **Ollama** — Local model runtime
* **Vision-Language Models** — LLaVA, Moondream, BakLLaVA, and more
* **Text Models** — Mistral, Llama 3, Gemma, and others

### 🔒 100% Local Processing

Unlike cloud-based AI services, **Insight Vision AI** processes everything on your machine:

✅ No API keys required  
✅ No data sent to external servers  
✅ Complete privacy and control  
✅ Works offline after model download  
✅ No usage limits or costs

---

# ✨ Key Features

## 🆕 **9 Powerful Workflows**

1. **Image Analysis** — Describe, OCR, identify objects, with EXIF metadata
2. **Document Chat** — Multi-turn Q&A across multiple documents
3. **Structured Extraction** — Extract custom fields from documents (invoices, resumes, contracts)
4. **Image + Document Cross-Analysis** — Ask questions spanning both image and document
5. **Batch Captioning** — Auto-caption multiple images, export to CSV
6. **Document Comparison** — Compare two document versions, identify changes
7. **Compare Images** — Side-by-side image comparison
8. **Code to Algorithm** — Convert code to flowcharts and explanations with interactive chat
9. **Algorithm to Code** — Generate code from descriptions in any language

---

# 🆕 New Features

### **🔍 EXIF Metadata Viewer**
- Extract camera make/model, exposure settings, date taken
- GPS coordinates with Google Maps integration
- Automatic display on image upload

### **📊 Batch Image Captioning**
- Process multiple images at once
- Choose caption style (descriptive, brief, social media, accessibility)
- Export to CSV with filename, dimensions, and captions
- Perfect for photo library cataloging

### **🔄 Document Comparison**
- Upload two document versions
- Identify added, removed, or modified content
- Compare modes: all changes, additions only, removals only, key differences
- Essential for contract reviews and version tracking

### **🖼️ + 📄 Image + Document Cross-Analysis**
- Upload both an image AND a document
- Ask questions spanning both sources
- Example: "Does this product photo match the spec sheet dimensions?"
- Perfect for compliance verification

### **💬 Code Explanation Chat**
- Multi-turn conversation about analyzed code
- Ask follow-up questions: "What does line 12 do?"
- Context-aware responses
- Export chat history

### **🎯 Prompt Template Library**
- Pre-built prompts for common tasks
- Categories: Image Analysis, Document Analysis, Code Analysis
- One-click prompt insertion
- Lowers barrier for new users

### **🔍 Code Language Auto-Detection**
- Automatically detects Python, JavaScript, Java, C++, and more
- Displays detected language before analysis
- Supports 10+ programming languages

### **💾 Export Full History**
- One-click JSON export of all history
- Includes workflows, prompts, results, timestamps
- Perfect for auditing and backup

### **🌐 Multi-Language AI Output**
- Generate in English, translate to 9 languages
- Two-step pipeline ensures accuracy
- Uses best text model for translation
- Supported: English, Hindi, Spanish, French, Arabic, Tamil, Bengali, German, Kannada

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.8+ | Core application |
| Streamlit | Web interface |
| Ollama | Local AI runtime |
| LLaVA / Moondream | Vision-language models |
| Mistral / Llama | Text processing models |
| Pillow | Image processing |
| SQLite | User accounts & history |
| Graphviz | Flowchart visualization |
| PyPDF, python-docx, openpyxl, python-pptx | Document extraction |

---

# 💻 System Requirements

### Minimum
- **OS:** Windows 10/11, Linux, macOS
- **RAM:** 8 GB
- **CPU:** Modern multi-core processor
- **Disk:** 10 GB free space (for models)

### Recommended
- **RAM:** 16 GB or more
- **GPU:** NVIDIA GPU with 6+ GB VRAM (for fast inference)
- **CPU:** 8+ cores
- **Disk:** SSD with 20+ GB free space

---

# 📋 Prerequisites

1. **Python 3.8+**
   ```bash
   python --version
   ```

2. **Ollama** — [Download from ollama.ai](https://ollama.ai)
   ```bash
   ollama --version
   ```

3. **Git** (for cloning repository)
   ```bash
   git --version
   ```

---

# 🚀 Installation

## Step 1 — Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd GEMINI_picture-text
```

## Step 2 — Create Virtual Environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4 — Install Ollama Models

### Vision Models (required for image tasks)
```bash
ollama pull llava
# or
ollama pull moondream
# or
ollama pull bakllava
```

### Text Models (recommended for better translation)
```bash
ollama pull mistral
# or
ollama pull llama3
```

## Step 5 — Verify Installation

```bash
ollama list
```

You should see your downloaded models listed.

---

# 🦙 Ollama Setup

### Start Ollama Server (if not running as service)

```bash
ollama serve
```

Keep this terminal open.

### Verify Ollama is Running

Open another terminal:

```bash
curl http://localhost:11434/api/tags
```

You should see JSON with your installed models.

---

# 🎯 Running the Application

### Start the Application

```bash
streamlit run picture.py
```

### Access in Browser

Open: **http://localhost:8501**

### First Time Setup

1. Click "Create account" tab
2. Enter username and password (min 10 characters)
3. Sign in
4. Select your preferred AI output language
5. Start analyzing!

---

# 📚 Complete Feature List

## 🖼️ Image Analysis

### Core Features
- Upload JPG, JPEG, PNG images
- Capture and add multiple photos directly from your device camera
- Multi-task analysis: describe, identify objects, OCR, translate text
- Custom prompts with template library
- Image resize and format options (preserve aspect ratio, never enlarge)
- EXIF metadata extraction and display
- GPS coordinates with Google Maps links

### EXIF Metadata Shown
- Camera make/model
- Date taken
- Exposure time
- ISO, aperture (F-number)
- Focal length
- Lens model
- GPS location (if available)

### Export Options
- .txt, .md, .json, Print HTML
- All results exportable

---

## 📄 Document Chat

### Supported Formats
- PDF (text-based)
- DOCX
- TXT
- XLSX (Excel)
- PPTX (PowerPoint)
- PPT (legacy, requires LibreOffice)

### Features
- Upload multiple documents
- Two modes:
  - **Chat:** Instant Q&A (RAG-based)
  - **Summarize:** Full summary + follow-up chat
- Multi-turn conversation with context
- Source citations (filename + part)
- Prompt templates for common tasks
- Clear chat and export options

---

## 🏗️ Structured Extraction

### Quick Templates
- **Resume:** Name, Email, Phone, Education, Experience, Skills
- **Invoice:** Number, Date, Vendor, Customer, Amount, Items
- **Contract:** Parties, Date, Term, Payment, Termination
- **Form:** Applicant, Date, Reference, Status

### Features
- Define unlimited custom fields
- Add/remove fields dynamically
- Field descriptions guide AI extraction
- Table format output
- Returns "Not found" for missing data
- Export as .txt, .md, .json, CSV

---

## 🖼️ + 📄 Image + Document Cross-Analysis

### Use Cases
- Product photo vs spec sheet verification
- Building photo vs architectural requirements
- Prototype vs design document comparison
- Equipment vs manual specifications

### Templates
- Verify Match
- Find Discrepancies
- Compliance Check
- Detailed Comparison

---

## 📸 Batch Captioning

### Caption Styles
- **Descriptive:** Clear, factual descriptions
- **Brief:** One-sentence captions
- **Detailed:** Comprehensive analysis
- **Social Media:** Engaging captions
- **Accessibility:** Screen reader-friendly

### Features
- Upload multiple images
- Progress bar with status
- CSV export with filename, dimensions, caption
- JSON export with full metadata
- Perfect for photo libraries, e-commerce, accessibility

---

## 🔄 Document Comparison

### Comparison Modes
- **All changes:** Complete diff
- **Added content:** New content in v2
- **Removed content:** Deleted from v1
- **Modified sections:** Changes between versions
- **Key differences:** Major changes only

### Use Cases
- Contract revisions
- Policy updates
- Report version tracking
- Legal document comparison
- Change logs

---

## 🖼️ Compare Images

### Features
- Upload 2+ images
- Custom comparison prompts
- Side-by-side analysis
- Vision model required
- Export comparison results

---

## 💻 Code to Algorithm

### Features
- Paste any code
- Auto-detect language (10+ languages)
- Generate plain-language algorithm
- Create Graphviz flowchart
- Interactive code chat
- Prompt templates:
  - Explain step-by-step
  - Find bugs
  - Optimize performance
  - Add documentation
  - Explain to beginner

### Code Chat
- Multi-turn conversation
- Ask about specific lines
- Request optimizations
- Context-aware responses
- Export chat separately

---

## 🔧 Algorithm to Code

### Features
- Written description or flowchart image input
- Target language selection:
  - Python, JavaScript, TypeScript
  - Java, C++, C#, Go, Rust
  - Custom language support
- Generates runnable code
- Code explanations included

---

# 🎯 Usage Guide

## Image Analysis

1. Click **"Image Analysis"** tool
2. Upload image(s) or use **Take a picture** and add each capture from your device camera
3. View EXIF metadata (if available)
4. Choose analysis tasks or use custom prompt
5. Optionally browse prompt templates
6. Click **"Analyse"**
7. View results and export

## Document Chat

1. Click **"Document Chat"** tool
2. Upload document(s)
3. Choose mode: Chat (instant) or Summarize (full)
4. **Chat mode:** Ask questions directly
5. **Summarize mode:** Get summary, then ask follow-ups
6. Export conversation or summaries

## Structured Extraction

1. Click **"Structured Extraction"** tool
2. Upload document
3. Select template or define custom fields
4. Add/edit/remove fields as needed
5. Click **"Extract Data"**
6. Review table output
7. Export as CSV or JSON

## Image + Document Cross-Analysis

1. Click **"Image + Document"** tool
2. Upload ONE image (left)
3. Upload ONE document (right)
4. Choose template or write custom question
5. Click **"Analyze Both"**
6. View cross-modal analysis
7. Export result

## Batch Captioning

1. Click **"Batch Captioning"** tool
2. Upload multiple images
3. Select caption style
4. Click **"Generate All Captions"**
5. Watch progress bar
6. Download CSV or JSON

## Document Comparison

1. Click **"Document Comparison"** tool
2. Upload Version 1 (original)
3. Upload Version 2 (updated)
4. Select comparison mode
5. Click **"Compare Documents"**
6. Review changes
7. Export comparison report

## Code Analysis

1. Click **"Code to Algorithm"** tool
2. Paste code
3. Note auto-detected language
4. Optionally use custom prompt or template
5. Click **"Generate algorithm & flowchart"**
6. View algorithm, flowchart, or chat tabs
7. Ask follow-up questions in Code Chat
8. Export results

## Code Generation

1. Click **"Algorithm to Code"** tool
2. Write description OR upload flowchart image
3. Select target language
4. Click **"Generate code"**
5. View generated code
6. Export or copy code

---

# 📋 Example Use Cases

### **Business**
- Invoice data extraction → accounting software
- Contract comparison before signing
- Meeting notes → action items
- Product photos vs specifications

### **Education**
- Code explanation for learning
- Document summarization for research
- Multi-language translation
- Accessibility descriptions

### **Content Creation**
- Batch photo captioning for social media
- Image descriptions for blogs
- Code documentation generation
- Flowchart creation

### **Legal/Compliance**
- Contract version comparison
- Document redline analysis
- Compliance verification (image + document)
- Evidence documentation

### **Development**
- Code-to-flowchart for documentation
- Algorithm-to-code for prototyping
- Bug finding and optimization
- Multi-language code generation

### **Photography**
- EXIF metadata review
- GPS location mapping
- Batch cataloging
- Image comparison

---

# 🛠️ Troubleshooting

## Ollama Connection Issues

**Problem:** Red "Ollama offline" indicator

**Solutions:**
1. Start Ollama: `ollama serve`
2. Check if running: `curl http://localhost:11434/api/tags`
3. Click "Refresh connection" in sidebar
4. Restart Ollama service

## Model Not Found

**Problem:** "Model 'llava' not found"

**Solutions:**
1. Pull model: `ollama pull llava`
2. Verify: `ollama list`
3. Restart app

## Vision Model Warnings

**Problem:** "Text-only model selected"

**Solutions:**
1. Image tasks require vision models (llava, moondream)
2. Select vision model from sidebar dropdown
3. Pull vision model if not installed

## Translation Not Working

**Problem:** "Translation returned empty"

**Solutions:**
1. Ensure text model is installed (mistral, llama3)
2. Check Ollama is running
3. Try different model from sidebar

## Timeout Errors

**Problem:** "Ollama timed out"

**Solutions:**
1. Use smaller images (reduce max dimension)
2. Select smaller model
3. Close other applications
4. Increase system resources
5. Use GPU if available

## Document Extraction Fails

**Problem:** "Could not read document"

**Solutions:**
1. Ensure document is not password-protected
2. For .ppt files, install LibreOffice
3. Check file is not corrupted
4. Try converting to PDF first

---

# ⚡ Performance

### Speed Tips

1. **Use GPU:** Ollama uses CUDA automatically if available
2. **Smaller models:** moondream is faster than llava
3. **Reduce image size:** Use 1024px max dimension
4. **Batch wisely:** Process 10-20 images at a time
5. **Close other apps:** Free up RAM

### Typical Processing Times (CPU)

- **Image analysis:** 30-90 seconds
- **Document summary:** 60-180 seconds
- **Code analysis:** 30-60 seconds
- **Batch captioning (10 images):** 5-15 minutes
- **Translation:** 10-30 seconds

### With GPU (NVIDIA)

- **Image analysis:** 5-15 seconds
- **Document summary:** 15-45 seconds
- **Code analysis:** 5-15 seconds
- **Batch captioning (10 images):** 1-3 minutes

---

# 🔐 Security and Privacy

### 100% Local Processing

✅ All AI processing happens on your machine  
✅ No data sent to external servers  
✅ No API keys or cloud accounts required  
✅ Complete control over your data  
✅ Works offline after setup

### Data Storage

- **Database:** `%LOCALAPPDATA%\InsightVisionAI\history.sqlite3` (Windows)
- **Contains:** User accounts, password hashes (PBKDF2), history
- **Does NOT store:** Uploaded files, images, documents
- **Backup:** Copy database file for backup

### Password Security

- Passwords hashed with PBKDF2 (310,000 iterations)
- Salt per user
- Never stored in plain text
- Minimum 10 characters required

### Network

- Application binds to localhost:8501 by default
- Ollama on localhost:11434
- No external network requests
- Safe for air-gapped environments

---

# 🚀 Future Enhancements

### Planned Features
- Save custom prompt templates to database
- Batch document processing
- Confidence scores for extractions
- Auto-detect document language
- Table/chart extraction with formatting
- Image annotation tools
- Dark/light theme toggle
- API endpoints for programmatic access

### Community Contributions Welcome!
- Submit issues for bugs
- Request features
- Contribute code
- Improve documentation
- Add more prompt templates

---

# 📜 License

This project is licensed under the MIT License.

See LICENSE file for details.

---

# ⭐ Acknowledgements

### Technologies
- **Streamlit** — Web framework
- **Ollama** — Local AI runtime
- **LLaVA** — Vision-language model
- **Mistral, Llama** — Text models
- **Pillow** — Image processing
- **PyPDF, python-docx** — Document processing

### Community
- Ollama team for amazing local AI runtime
- LLaVA researchers for open vision model
- Streamlit team for excellent framework
- Open source community

---

# 🎉 Quick Start Summary

```bash
# Install Ollama from ollama.ai

# Pull models
ollama pull llava
ollama pull mistral

# Clone and setup
git clone <REPO_URL>
cd GEMINI_picture-text
python -m venv .venv
.venv\Scripts\activate  # Windows
# or: source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Run
streamlit run picture.py
```

**Open:** http://localhost:8501

**Create account** → **Start analyzing!**

---

## 🌟 Project Highlights

✅ **9 distinct workflows** covering images, documents, and code  
✅ **Cross-modal analysis** (image + document simultaneously)  
✅ **Batch processing** with CSV export  
✅ **Structured data extraction** with templates  
✅ **Interactive code chat** for learning  
✅ **20+ prompt templates** for ease of use  
✅ **EXIF metadata** with GPS mapping  
✅ **Multi-language** AI output  
✅ **100% local** — complete privacy  
✅ **Professional UI** — dark theme, modern design  

**Insight Vision AI** — The complete local AI solution for images, documents, and code.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Key Features](#-key-features)
* [Technologies Used](#-technologies-used)
* [System Requirements](#-system-requirements)
* [Prerequisites](#-prerequisites)
* [Project Structure](#-project-structure)
* [Installation](#-installation)
* [Ollama Setup](#-ollama-setup)
* [Download LLaVA Model](#-download-llava-model)
* [Running the Application](#-running-the-application)
* [How the Application Works](#-how-the-application-works)
* [Application Workflow](#-application-workflow)
* [Features in Detail](#-features-in-detail)
* [Ollama API](#-ollama-api)
* [Configuration](#-configuration)
* [Requirements File](#-requirements-file)
* [Usage](#-usage)
* [Example Prompts](#-example-prompts)
* [Troubleshooting](#-troubleshooting)
* [Performance](#-performance)
* [Security and Privacy](#-security-and-privacy)
* [Limitations](#-limitations)
* [Future Enhancements](#-future-enhancements)
* [Project Architecture](#-project-architecture)
* [Commands Summary](#-commands-summary)
* [License](#-license)

---

# 📖 Overview

**Local Vision AI** is a local image-question-answering application that combines:

* **Streamlit** — Web-based user interface
* **Python** — Application logic
* **Ollama** — Local model runtime
* **LLaVA** — Vision-language AI model

The user uploads an image through the Streamlit interface and enters a question or prompt.

The application converts the image into a Base64-encoded representation and sends it to the locally running Ollama server. Ollama passes the image to LLaVA, which analyzes the visual content and generates a natural-language response.

### 🔒 Fully Local Processing

Unlike applications that use cloud-based vision APIs, this project is designed to process the image locally.

The application communicates with:

```text
Streamlit Application
        ↓
Python
        ↓
Ollama API
        ↓
LLaVA Model
        ↓
Generated Response
```

No API key is required.

---

# ✨ Key Features

## 1. 🖼️ Image Upload

Users can upload images directly through the Streamlit interface.

Supported formats:

* JPG
* JPEG
* PNG

Example:

```text
📤 Upload image
```

The uploaded image is converted to RGB format before processing.

In Image Understanding, Compare Images, and flowchart-image input, the **Resize and format options** let users keep the original dimensions or set a maximum image dimension, choose JPEG or PNG output, and adjust JPEG quality. Resizing preserves the aspect ratio and never enlarges an image. The prepared images are used for local model input and can also be downloaded. Image Evidence Review continues to use the uploaded image at its original dimensions.

---

## 2. 👁️ Image Understanding

The LLaVA model can analyze the contents of an uploaded image.

Depending on the image and prompt, it can identify or describe:

* Objects
* People
* Animals
* Scenes
* Text visible in images
* Colors
* Basic relationships between objects
* General image descriptions
* Visual context

---

## 3. 💬 Ask Questions About Images

Users can enter natural-language questions such as:

```text
What is present in this image?
```

or:

```text
Describe this image.
```

or:

```text
How many people are visible?
```

The question is sent to LLaVA together with the image.

---

## 4. 🧠 Local AI Processing

The application uses Ollama to run LLaVA locally.

This means:

* No OpenAI API required
* No Gemini API required
* No cloud vision API required
* No API key required
* Image processing can be performed locally

The only external requirement is the locally installed Ollama software and the downloaded model.

---

## 5. 💬 Accounts and Persistent History

Users create an account and sign in. Each user's analysis prompts and results are saved in a local SQLite database and can be viewed or deleted from the History panel. Uploaded image files are not saved in the history database. Passwords are stored as salted PBKDF2 hashes, not as plain text.

On Windows, the database is stored at `%LOCALAPPDATA%\LocalVisionAI\history.sqlite3`. On other platforms it is stored at `~/.local/share/LocalVisionAI/history.sqlite3`.

## 6. 🌐 AI Output Languages

The app interface remains in English. After signing in, choose Hindi, Spanish, French, Arabic, Tamil, Bengali, German, or Kannada from the **AI output language** selector. The selected preference is saved for that account and applies to new AI-generated explanations and image-analysis responses. Translation quality depends on the selected local model, so review important wording.

---

## 7. 📄 Document Analysis

Choose **Document analysis** to upload multiple PDF, DOCX, TXT, XLSX, PPTX, or legacy PPT files. The app extracts text locally, generates a summary for each document, and lets you ask questions across the uploaded documents. Answers are grounded in relevant document excerpts and include source filenames and parts. The selected AI output language applies to summaries and answers.

PDFs and Office files must contain extractable text; scanned image-only PDFs are not OCR-processed. Legacy `.ppt` files require LibreOffice to be installed and available on `PATH`. Uploaded file contents are held in the app session and are not stored in the history database; history stores the resulting summaries and answers.

---

## 8. ⚡ Simple Streamlit Interface

The interface contains:

* Application title
* Description
* Prompt input
* Image uploader
* Uploaded image preview
* Ask AI button
* Persistent per-account history
* Footer

---

## 8. 🛡️ Input Validation

The application checks whether:

* An image has been uploaded
* A prompt has been entered

If either is missing, the application displays an appropriate warning.

Example:

```text
Please upload an image
```

or:

```text
Please enter a prompt
```

---

# 🛠️ Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Core application development   |
| Streamlit  | Web UI                         |
| Ollama     | Local AI model runtime         |
| LLaVA      | Vision-language model          |
| Pillow     | Image processing               |
| Requests   | HTTP communication with Ollama |
| Base64     | Image encoding                 |
| io         | In-memory image processing     |

---

# 💻 System Requirements

Recommended environment:

### Operating System

The project can run on:

* Windows
* Linux
* macOS

### Hardware

For reasonable performance, a system with:

* Modern multi-core CPU
* At least 8 GB RAM
* 16 GB RAM recommended
* Sufficient disk space for the AI model

A compatible GPU can significantly improve inference performance.

---

# 📋 Prerequisites

Before running the project, install:

1. Python
2. pip
3. Ollama
4. LLaVA model

Verify Python:

```bash
python --version
```

or:

```bash
python3 --version
```

Verify pip:

```bash
pip --version
```

Verify Ollama:

```bash
ollama --version
```

---

# 📁 Project Structure

A simple project structure is sufficient:

```text
Local-Vision-AI/
│
├── app.py
├── requirements.txt
└── README.md
```

Where:

### `app.py`

Contains the complete Streamlit application.

### `requirements.txt`

Contains Python dependencies.

### `README.md`

Contains project documentation and setup instructions.

---

# 🐍 Installation

## Step 1 — Clone the Repository

If the project is hosted on GitHub:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Local-Vision-AI
```

---

# Step 2 — Create a Virtual Environment

Creating a virtual environment is recommended.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

You should see something similar to:

```text
(venv)
```

in your terminal.

### Linux/macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Step 3 — Install Python Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a requirements file yet, install the dependencies manually:

```bash
pip install streamlit pillow requests
```

---

# 🦙 Ollama Setup

Ollama is responsible for running the AI model locally.

Install Ollama on your operating system and verify the installation:

```bash
ollama --version
```

The application communicates with Ollama using:

```text
http://localhost:11434
```

The Ollama API endpoint used by this application is:

```text
/api/generate
```

Therefore, the complete endpoint is:

```text
http://localhost:11434/api/generate
```

---

# 👁️ Download LLaVA Model

The application is configured to use:

```text
llava
```

Download the model using:

```bash
ollama pull llava
```

This downloads the LLaVA model required for image understanding.

---

# 🔍 Verify LLaVA Installation

Check the models installed in Ollama:

```bash
ollama list
```

You should see LLaVA listed.

For example:

```text
NAME      ID       SIZE
llava     ...      ...
```

You can also test the model directly:

```bash
ollama run llava
```

If the model starts successfully, Ollama is ready.

Exit the model using:

```text
/bye
```

---

# 🚀 Running the Application

There are two components that need to work:

```text
Ollama
+
Streamlit
```

## Step 1 — Start Ollama

On systems where Ollama is not already running as a background service, start it with:

```bash
ollama serve
```

Keep this terminal running.

---

## Step 2 — Open Another Terminal

Navigate to your project directory:

```bash
cd Local-Vision-AI
```

Activate the virtual environment if you created one:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Step 3 — Run Streamlit

Run:

```bash
streamlit run app.py
```

Streamlit will start the local web server.

You will typically see a message similar to:

```text
Local URL: http://localhost:8501
```

Open the displayed address in your browser.

---

# ⚡ Quick Start

If everything is already installed, the basic commands are:

```bash
ollama pull llava
```

Then:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Upload an image, enter a question, and click:

```text
🚀 Ask AI
```

---

# 🔄 How the Application Works

The application follows the following process:

```text
User
 │
 │ Upload Image
 ▼
Streamlit UI
 │
 │ Enter Prompt
 ▼
Python Application
 │
 │ Convert Image → JPEG
 ▼
Base64 Encoding
 │
 ▼
Ollama REST API
 │
 │ model = llava
 ▼
LLaVA Vision Model
 │
 │ Analyze Image + Prompt
 ▼
Generated Response
 │
 ▼
Streamlit
 │
 ▼
Chat History
```

---

# 🧩 Application Workflow

## Step 1 — User Uploads Image

The image is uploaded using Streamlit:

```python
uploaded_file = st.file_uploader(
    "📤 Upload image",
    type=["jpg", "jpeg", "png"]
)
```

---

## Step 2 — Image Conversion

The image is opened using Pillow:

```python
image = Image.open(uploaded_file).convert("RGB")
```

This ensures that the image is converted into RGB format.

---

## Step 3 — Image Encoding

The image is temporarily stored in memory:

```python
buf = io.BytesIO()
image.save(buf, format="JPEG")
```

The image bytes are then converted into Base64:

```python
img_b64 = base64.b64encode(
    buf.getvalue()
).decode()
```

---

## Step 4 — API Payload

The application creates the Ollama request:

```python
payload = {
    "model": "llava",
    "prompt": prompt,
    "images": [img_b64],
    "stream": False
}
```

The payload contains:

* Model name
* User prompt
* Base64 encoded image
* Streaming configuration

---

## Step 5 — Send Request to Ollama

Python sends an HTTP POST request:

```python
requests.post(
    "http://localhost:11434/api/generate",
    json=payload
)
```

---

## Step 6 — LLaVA Processes the Image

Ollama passes the image and prompt to LLaVA.

LLaVA performs visual-language reasoning and generates a textual answer.

---

## Step 7 — Display Response

The response is extracted:

```python
response.json()["response"]
```

The answer can be saved to the signed-in user's local history database.

---

# 🧠 Features in Detail

## Local Vision Model

The project uses:

```text
LLaVA
```

LLaVA is a multimodal vision-language model capable of accepting both text and image information.

The model allows users to interact with images using natural language.

---

## Per-Account Persistent History

Prompts and generated results are stored in SQLite and remain available after restarting the app. Each signed-in account can view and delete only its own history. Uploaded image files are not stored in the history database.

---

# 🔌 Ollama API

The project uses the Ollama local REST API.

### Endpoint

```text
POST http://localhost:11434/api/generate
```

### Request

The request contains:

```json
{
    "model": "llava",
    "prompt": "Describe this image",
    "images": [
        "BASE64_ENCODED_IMAGE"
    ],
    "stream": false
}
```

### Response

Ollama returns a JSON response containing the generated text.

The application extracts:

```python
response.json()["response"]
```

---

# ⚙️ Configuration

The Streamlit page is configured using:

```python
st.set_page_config(
    page_title="Local Vision AI (Ollama)",
    page_icon="🧠",
    layout="wide"
)
```

### Page Title

```text
Local Vision AI (Ollama)
```

### Page Icon

```text
🧠
```

### Layout

```text
wide
```

---

# 📦 Requirements File

Create a file named:

```text
requirements.txt
```

Add:

```text
streamlit
Pillow
requests
```

You can then install all dependencies using:

```bash
pip install -r requirements.txt
```

For reproducible environments, you can also generate a pinned requirements file after installation:

```bash
pip freeze > requirements.txt
```

---

# 🖥️ Usage

After launching the application:

## 1. Upload an Image

Click:

```text
📤 Upload image
```

Select:

```text
.jpg
.jpeg
.png
```

---

## 2. Enter a Prompt

Enter a question in:

```text
💬 Ask something about the image
```

Example:

```text
Describe this image in detail.
```

---

## 3. Click Ask AI

Click:

```text
🚀 Ask AI
```

The application will display:

```text
Thinking locally... 🧠
```

while LLaVA processes the request.

---

## 4. View the Response

The generated answer will appear under:

```text
💬 Chat History
```

---

# 💡 Example Prompts

You can ask questions such as:

### General Description

```text
Describe this image.
```

### Object Detection

```text
What objects are present in this image?
```

### Counting

```text
How many people are visible?
```

### Scene Understanding

```text
What is happening in this image?
```

### Environment

```text
Is this image taken indoors or outdoors?
```

### Colors

```text
What are the main colors in this image?
```

### Detailed Description

```text
Describe the image in detail, including the objects, people, background and surroundings.
```

### Specific Object

```text
Is there a car in this image?
```

### Text

```text
What text can you read in this image?
```

---

# 🛠️ Troubleshooting

## Problem 1 — `streamlit` is not recognized

If you see:

```text
'streamlit' is not recognized as an internal or external command
```

Install Streamlit:

```bash
pip install streamlit
```

Then run:

```bash
python -m streamlit run app.py
```

Using the Python module form is often more reliable on Windows.

---

# Problem 2 — `ollama` is not recognized

If you see:

```text
'ollama' is not recognized
```

Install Ollama and restart the terminal.

Then verify:

```bash
ollama --version
```

---

# Problem 3 — Connection refused

If you receive an error similar to:

```text
Connection refused
```

the Ollama server may not be running.

Start it:

```bash
ollama serve
```

Then run Streamlit again.

---

# Problem 4 — LLaVA model not found

If Ollama reports that the model is unavailable, run:

```bash
ollama pull llava
```

Then verify:

```bash
ollama list
```

---

# Problem 5 — Very Slow Responses

LLaVA is a relatively large vision-language model.

Response speed depends on:

* CPU
* GPU
* RAM
* Image resolution
* Model size
* Number of concurrent requests
* Available system resources

If processing takes several minutes, check system resource usage.

A GPU-supported Ollama setup can significantly improve performance.

---

# Problem 6 — Browser Does Not Open

Run:

```bash
streamlit run app.py
```

Then manually open:

```text
http://localhost:8501
```

---

# Problem 7 — Python Version Issues

Check:

```bash
python --version
```

If packages fail to install, use a supported Python version and recreate the virtual environment.

---

# 🔐 Security and Privacy

One of the main goals of this project is local processing.

The application sends image-analysis and translation requests to:

```text
localhost:11434
```

rather than a cloud AI service.

Therefore, images are intended to remain within the local machine's Ollama workflow.
Account records, password hashes, analysis prompts/results, and AI output language preferences are stored in the local SQLite database described above. The app does not store uploaded image files in history.

### Important

Local processing does not automatically mean the application is secure in every deployment scenario. If Ollama or Streamlit is exposed beyond the local machine, additional network and access controls should be implemented.

---

# ⚠️ Limitations

The current implementation has several limitations.

## 1. Local Accounts and History

Account information, saved prompts/results, and AI output language preferences are stored in the local SQLite database. The history is associated with the signed-in local account. Back up this database if you need to preserve it across device changes. This simple local account system is intended for a locally run app; it is not a substitute for production-grade authentication when exposing the app to a network.

---

## 2. Local-Only Accounts

Accounts and history are local to this computer and are not synchronized between devices. This simple account system is intended for local use and is not production-grade authentication for an internet-facing deployment.

---

## 3. AI Output Translation

The selected output language applies to new AI-generated results. It does not translate the app interface or previously saved results.

---

## 4. Document Text Extraction

Document summaries and answers use extractable text from uploaded files. Scanned PDFs and embedded images are not OCR-processed, and legacy `.ppt` conversion requires LibreOffice.

---

## 5. Model Performance Depends on Hardware

LLaVA inference can be slow on systems without suitable GPU acceleration.

---

## 5. Vision Model Accuracy

The generated response may sometimes be incorrect.

Users should not treat model output as guaranteed ground truth, particularly for:

* Medical images
* Safety-critical images
* Legal evidence
* Security decisions
* Financial documents

---

# 🚀 Future Enhancements

The project can be extended with several features.

### 1. Multiple Image Support

Allow users to upload multiple images and compare them.

---

### 2. Voice Input

Add speech-to-text functionality so users can ask questions verbally.

---

### 3. Text-to-Speech

Convert LLaVA responses into speech.

---

### 4. Download Chat History

Add buttons to download conversations as:

```text
TXT
PDF
JSON
CSV
```

---

### 5. Persistent Database

Store conversations in:

```text
SQLite
MySQL
PostgreSQL
MongoDB
```

---

### 6. Model Selection

Allow users to select different Ollama models from the UI.

Example:

```text
llava
llama3
mistral
```

Only models capable of the required task should be used for image analysis.

---

### 7. Advanced Vision Pipeline

A future version could combine:

```text
YOLO
+
LLaVA
+
OCR
+
Text-to-Speech
```

For example:

```text
Image
  ↓
YOLO Object Detection
  ↓
Detected Objects
  ↓
LLaVA Contextual Understanding
  ↓
OCR
  ↓
Final Description
  ↓
Text-to-Speech
```

This would make the application more suitable for advanced accessibility and computer-vision applications.

---

# 🏗️ Project Architecture

```text
                 ┌─────────────────────┐
                 │       User          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Streamlit UI    │
                 │                     │
                 │ Image Upload        │
                 │ Prompt Input        │
                 │ Chat History        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Python Backend    │
                 │                     │
                 │ Pillow              │
                 │ Base64              │
                 │ Requests            │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Ollama Server    │
                 │ localhost:11434     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       LLaVA         │
                 │ Vision-Language AI  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Generated Response  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Chat History UI   │
                 └─────────────────────┘
```

---

# 🔄 Complete Data Flow

```text
Image Upload
     ↓
Pillow Image.open()
     ↓
Convert to RGB
     ↓
Convert image to JPEG
     ↓
Base64 Encoding
     ↓
Create JSON Payload
     ↓
POST Request
     ↓
Ollama API
     ↓
LLaVA
     ↓
Image + Prompt Analysis
     ↓
Text Response
     ↓
Streamlit
     ↓
Session State
     ↓
Chat History
```

---

# 📋 Commands Summary

## Check Python

```bash
python --version
```

## Create virtual environment

```bash
python -m venv venv
```

## Activate virtual environment — Windows

```bash
venv\Scripts\activate
```

## Activate virtual environment — Linux/macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install streamlit pillow requests
```

## Check Ollama

```bash
ollama --version
```

## Download LLaVA

```bash
ollama pull llava
```

## Check installed models

```bash
ollama list
```

## Run Ollama server

```bash
ollama serve
```

## Test LLaVA

```bash
ollama run llava
```

## Run Streamlit

```bash
streamlit run app.py
```

Alternative:

```bash
python -m streamlit run app.py
```

## Open application

```text
http://localhost:8501
```

---

# 🧪 Basic Testing Checklist

Before using the application, verify:

* [ ] Python is installed
* [ ] pip is working
* [ ] Ollama is installed
* [ ] Ollama server is running
* [ ] LLaVA is downloaded
* [ ] `requirements.txt` dependencies are installed
* [ ] `app.py` exists
* [ ] Streamlit starts successfully
* [ ] Browser can access `localhost:8501`
* [ ] Image upload works
* [ ] Prompt input works
* [ ] LLaVA returns a response
* [ ] Chat history is displayed

---

# 📌 Example Complete Setup

On a fresh Windows machine, the workflow can look like:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Local-Vision-AI

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

ollama pull llava

ollama serve
```

Open another terminal:

```bash
cd Local-Vision-AI
venv\Scripts\activate

streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# 📄 Main Files

| File               | Description                 |
| ------------------ | --------------------------- |
| `app.py`           | Main Streamlit application  |
| `requirements.txt` | Python package dependencies |
| `README.md`        | Project documentation       |

---

# 🎯 Project Objective

The primary objective of this project is to develop a simple, privacy-oriented **local vision AI application** that enables users to interact with images using natural language.

The project demonstrates the integration of:

```text
Python
+
Streamlit
+
REST API
+
Ollama
+
LLaVA
+
Computer Vision
```

without depending on a paid cloud AI API.

---

# 🌟 Project Highlights

* 🧠 Local Vision AI
* 🦙 Ollama integration
* 👁️ LLaVA image understanding
* 🖼️ JPG/JPEG/PNG support
* 💬 Natural-language image queries
* 📚 Per-account persistent history
* 🔒 Local processing architecture
* 🚫 No API key required
* 🌐 Streamlit web interface
* 🐍 Python-based implementation

---

# 📜 License

This project can be released under the MIT License.

If using the MIT License, create a file named:

```text
LICENSE
```

and add the appropriate MIT License text.

---

# ⭐ Acknowledgements

This project makes use of:

* Streamlit for the web interface
* Ollama for local model execution
* LLaVA for vision-language processing
* Pillow for image processing
* Requests for API communication

---

## 🚀 Final Quick Command

Once everything has been installed and Ollama is available, the main command to launch the project is:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

Upload an image → Enter a question → Click **🚀 Ask AI** → Get the response from **LLaVA locally**.
