import PyPDF2
import re
import os

# Define important keywords to look for
keywords = ["Python", "C", "C++", "SQL", "Git", "GitHub", "AWS", "Cloud", "Excel", "Machine Learning", "Linux", "IoT"]

# Ask the user to enter their resume path (PDF Format)
resume_path = input("📁 Enter the path to your resume PDF file (e.g., resume.pdf): ")

if not os.path.isfile(resume_path):
    print("❌ File does not exist. Please check the name or path.")
    exit()

try:
    with open(resume_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()  # <-- FIXED: add () to extract_text
except PermissionError:
    print("❌ Permission denied. Close the file if it's open somewhere and try again.")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")
    exit()

# Analyze the resume
print("\n📊 Resume Analyzer Report")
print("-" * 40)

# Total Pages
print(f"📄 Total pages: {len(pdf_reader.pages)}")  # <-- FIXED: use f-string properly

# Search for keywords
found = []
missing = []

for word in keywords:
    if re.search(rf"\b{word}\b", full_text, re.IGNORECASE):
        found.append(word)
    else:
        missing.append(word)

print(f"\n✅ Found Keywords: {', '.join(found) if found else 'None'}")

# 🎓 Education Section Check
if re.search(r"(education|academic background|qualifications)", full_text, re.IGNORECASE):
    print("\n🎓 Education Section: ✅ Found")
else:
    print("\n🎓 Education Section: ❌ Not Found")

# Suggestions
print("\n💡 Suggestions:")
if len(found) < 5:
    print("➕ Add more technical keywords relevant to the job you're applying for.")
if "Git" not in found or "GitHub" not in found:
    print("🔧 Mention Git or GitHub if you've used version control.")
if "AWS" not in found and "Cloud" not in found:
    print("☁️ Learn Cloud basics like AWS or Azure.")
if "Machine Learning" not in found and "Data Science" not in found:
    print("🧠 Add ML/AI/Data projects if you're interested in that domain.")

print("\n✅ Done! Your resume just got analyzed like a boss 🧠🚀")
