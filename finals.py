import requests # [cite: 22]

# Τοπικό URL από το XAMPP [cite: 25, 32]
LOCAL_URL = "http://localhost/wordpress/wp-json/wp/v2/posts"

def fetch_local_posts():
    print(f"Σύνδεση στο τοπικό WordPress: {LOCAL_URL}") # [cite: 51]
    try:
        # Λήψη δεδομένων (μόνο τα 3 τελευταία) [cite: 52, 53]
        response = requests.get(LOCAL_URL, params={'per_page': 3}, timeout=5)
        
        if response.status_code == 200: # [cite: 54]
            posts = response.json() # [cite: 55]
            print(f"Βρέθηκαν {len(posts)} πρόσφατα άρθρα:\n") # [cite: 56]
            for post in posts: # [cite: 57]
                # Εμφάνιση ID και Τίτλου [cite: 59]
                print(f"ID: {post['id']} | Τίτλος: {post['title']['rendered']}")
        else:
            print("Σφάλμα: Το WordPress API δεν απαντά. Ελέγξτε αν το XAMPP είναι ανοιχτό.") # [cite: 58, 60]
    except Exception as e:
        print(f"Αποτυχία σύνδεσης: {e}") # [cite: 61, 62]

if __name__ == "__main__": # [cite: 49, 63]
    fetch_local_posts() # [cite: 64]
