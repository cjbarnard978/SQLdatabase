# OCR and AI correction with Tesseract and OpenAI

This script is a Python loop designed to provide OCR of historical documents. Using Tesseract OCR and OpenAI, it analyzes the confidence of each page of OCRed text and passes any with a confidence level of below 65% to OpenAI's gpt-3.5-turbo for correction. 

IMPORTANT: This script is not designed to analyze and OCR handwriting. It will only provide accurate results and run as intended if the PDFs included are typed. 

# Installing Tesseract 

On Mac: brew install tesseract on the command line

For more information and other operating systems consult tesseract-ocr.github.io/tessdoc/installation.html

To install other necessary packages see requirements.txt 

# How to Create and Activate a Virtual Environment 

Once in appropriate directory run python3 -m venv my_env in the terminal. 

to deploy: source my_env/bin/activate

# OpenAI API Key Instructions 

Create an OpenAI account using the email linked to the project.

Go to platform-openai.com/docs/quickstart/create-and-export-an-open-ai-key

Click the "Create an API Key" button. 

Make sure to copy and save your API key somewhere on your machine. If you forget your API key, delete the old one and generate a new one. 

IMPORTANT: DO NOT PUSH YOUR API KEY TO GITHUB. When pushing to github replace your secret API key with a placeholder-this script uses 'yourkeyhere' 

# How the Script Works 

First, the script will ensure you have the correct packages installed in your virtual environment. Make sure to check requirements.txt. Next, any PDF in your PDF directory will be passed to pdf2image, then separated into individual pngs. It is important to note that the only image refinement in this script is a convert to grayscale path-this is because the script is geared toward scanned images of aged books that may be yellowed, but are otherwise well scanned. Once the images are converted to grayscale and moved to a separate directory, that directory sends the grayscale images to pytesseract using a for/if loop. If the OCR confidence rating is less than 65% in pytesseract, the loop passes the OCR file to a low confidence directory and continues through the grayscale directory. Once the OCR is complete, images in the low confidence directory are passed to openai 0.28 for AI correction. Finally, the corrected OCR files are passed to a directory called openai_corrections. You will know the loop is complete when "'Corrected text saved to {corrected_file}" prints to your terminal. 

A note on notes: Added context remains in the script itself through the code when extra explanation benefits the use case, such as how the loop sorts through blank .txt files. It was an unfamiliar structure for me, so I chose to leave it in for others who might encounter the same issue. 