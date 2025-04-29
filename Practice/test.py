import csv
import json
import os

# Global ISO map (loaded later)
ISO_COUNTRIES = {}

# Step 1: Create sample ISO country file
def create_iso_country_file():
    os.makedirs("data", exist_ok=True)
    with open("data/iso_countries.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["code", "name"])
        writer.writerows([
            ["IN", "India"],
            ["US", "United States"],
            ["UK", "United Kingdom"],
            ["CA", "Canada"],
            ["AU", "Australia"],
            ["DE", "Germany"],
            ["FR", "France"],
            ["JP", "Japan"],
            ["CN", "China"],
            ["BR", "Brazil"],
            ["ZA", "South Africa"],
            ["MX", "Mexico"],
            ["RU", "Russia"]
        ])
    print("✅ ISO country codes file created.\n")

# Step 2: Load ISO country codes into dict
def load_iso_country_codes():
    iso_map = {}
    try:
        with open("data/iso_countries.csv", mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                code = row["code"].strip().upper()
                name = row["name"].strip()
                iso_map[code] = name
        print("🌍 Loaded ISO country codes.")
    except FileNotFoundError:
        print("❌ ISO country file not found!")
    return iso_map

# Step 3: Create sample candidate data
def create_sample_data():
    os.makedirs("data", exist_ok=True)

    with open("data/basicInfo.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["candidate_id", "name", "email", "phone", "loc1", "loc2", "loc3"])
        writer.writerow(["101", "Alice", "alice@example.com", "1234567890", "loc-city-Blr", "loc-state-Karnataka", "loc-country-IN"])
        writer.writerow(["102", "Bob", "bob@example.com", "0987654321","","loc-country-US", "loc-city-Dallas"])
        writer.writerow(["103", "Charlie", "charlie@example.com", "1112223333", "loc-country-IN", "loc-state-as", "bad-format-abc"])
        writer.writerow(["104", "David", "david@example.com", "4445556666", "", "", ""])

    with open("data/exp.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["candidate_id", "company", "title", "years"])
        writer.writerow(["101", "Google", "SWE", "2"])
        writer.writerow(["101", "Amazon", "Developer", "1"])
        writer.writerow(["102", "Microsoft", "PM", "3"])
        writer.writerow(["104", "Meta", "Analyst", "1"])

    with open("data/ed.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["candidate_id", "degree", "university", "year"])
        writer.writerow(["101", "B.Tech", "IIT Delhi", "2018"])
        writer.writerow(["102", "MBA", "IIM Bangalore", "2019"])
        writer.writerow(["102", "B.Com", "Delhi University", "2016"])
        writer.writerow(["104", "BSc", "Anna University", "2020"])

    print("✅ Sample candidate data created.\n")

# Step 4: Group CSV rows by candidate_id
def read_csv_grouped_by_id(filename, key_field):
    grouped = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cid = row[key_field]
            if cid not in grouped:
                grouped[cid] = []
            grouped[cid].append(row)
    print(f"📄 Loaded and grouped data from {filename}")
    return grouped

# Step 5: Parse location fields with strict validation
def parse_address_fields(row):
    address = {}
    for field in ["loc1", "loc2", "loc3"]:
        value = row.get(field, "").strip()
        if value:
            parts = value.split("-")
            if len(parts) == 3 and parts[0] == "loc":
                key, raw_val = parts[1].lower(), parts[2].strip()

                if key == "country":
                    full_country = ISO_COUNTRIES.get(raw_val.upper())
                    if full_country:
                        address["country"] = full_country
                        print(f"🌍 Valid country code: {raw_val} → {full_country}")
                    else:
                        print(f"⚠️ Invalid country ISO code in {field}: {raw_val} (ignored)")
                elif key in ["city", "state"] and raw_val:
                    address[key] = raw_val
                    print(f"🏙️ Valid {key}: {raw_val}")
                else:
                    print(f"⚠️ Invalid key or empty value in {field}: {value} (ignored)")
            else:
                print(f"⚠️ Skipping malformed location: {value}")
    return address

# Step 6: Generate JSON files per candidate
def generate_json_files():
    basic_info = {}
    with open("data/basicInfo.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cid = row["candidate_id"]
            print(f"\n🔍 Parsing basic info for candidate {cid}")
            info = {
                "candidate_id": cid,
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"]
            }

            address = parse_address_fields(row)
            if address:
                info["address"] = address
                print(f"📦 Address compiled: {address}")
            else:
                print("📭 No valid address extracted.")

            basic_info[cid] = info

    print("\n✅ Basic info parsed.\n")

    exp_info = read_csv_grouped_by_id("data/exp.csv", "candidate_id")
    ed_info = read_csv_grouped_by_id("data/ed.csv", "candidate_id")

    os.makedirs("output_json", exist_ok=True)

    for cid in basic_info:
        print(f"\n🛠️ Compiling final JSON for candidate ID: {cid}")
        compiled = {
            "basic_info": basic_info[cid],
            "experience": exp_info.get(cid, []),
            "education": ed_info.get(cid, [])
        }

        json_filename = f"output_json/{cid}.json"
        with open(json_filename, mode='w') as f:
            json.dump(compiled, f, indent=4)

        print(f"✅ JSON written to {json_filename}")

# Step 7: Run the full pipeline
if __name__ == "__main__":
    create_iso_country_file()
    create_sample_data()
    ISO_COUNTRIES = load_iso_country_codes()
    generate_json_files()