def classify_document(text):
    text = text.lower()

    categories = {
        "HR": ["employee", "salary", "leave", "recruitment"],
        "Finance": ["invoice", "payment", "tax", "budget"],
        "Operations": ["process", "workflow", "logistics"],
        "Legal": ["agreement", "contract", "law", "compliance"]
    }

    for category, keywords in categories.items():
        for word in keywords:
            if word in text:
                return category

    return "Unknown"
