import os
from datetime import datetime

def generate_cps_document():
    # Pre-populated personal data for Rikesh Prasad Lal
    full_name = "Rikesh Prasad Lall"
    sons = "Niam and Zen"
    date_str = "May 19, 2026"  # User's Birthday
    
    print("--- Supplydimezzz Legal Records Pipeline ---")
    print(f"Generating formal statement for {full_name} on {date_str}...")
    
    # Prompting only for the necessary missing contact details
    worker_name = input("\nEnter Social Worker's Name (or hit Enter for 'Assigned Social Worker'): ") or "Assigned Social Worker"
    wife_name = input("Enter Wife's Name (Anushka): ") or "Anushka"
    phone_num = input("Enter your phone number: ")
    
    document_content = f"""Date: {date_str}
To: {worker_name} / Sacramento County Department of Child, Family and Adult Services (DCFAS)
Cc: {wife_name}
Subject: Formal Statement and Protective Capacity Review Request - Rikesh Prasad Lal

To Whom It May Concern,

I am writing to formally clarify my position regarding the current voluntary safety inquiries by Child Protective Services and to ensure my full, peaceful cooperation is accurately documented in my case file.

Please accept this document as my official statement:

1. Absolute Commitment to My Children: My primary, unconditional priority is the safety, emotional well-being, and stability of my two sons, {sons}. I love my children deeply, and my goal is to maintain a peaceful, positive, and protective environment for them. 

2. Status of Legal Mandates: I note for the official record that there is currently no active juvenile dependency court order or family law court order mandating separation, restricted contact, or compulsory class enrollment. This remains a voluntary administrative process.

3. Position on Proposed Requirements: While I am fully willing to cooperate with factual, objective assessments regarding my children’s welfare, I respectfully decline to enroll in general parenting or domestic violence classes at this time. I am a victim of multiple forms of documented domestic and emotional abuse in this situation, and I maintain my complete innocence regarding any allegations of child neglect or harm. Enrolling in these classes under the current framing inaccurately implies an admission of risks I did not create, which could compromise my position in upcoming family law proceedings.

4. Alternative Proposals for Verifiable Cooperation: In the spirit of transparency, peace, and positivity, I am fully prepared to immediately engage in the following alternative measures to demonstrate my protective capacity to the department:
   - Facilitating scheduled or unannounced wellness checks by the department or local law enforcement to verify the continuous safety and happiness of the children while in my care.
   - Submitting my organized evidence files, including relevant police reports and historical records, to factually demonstrate the true dynamics of the abuse occurring in our household environment.
   - Requesting a formal case review meeting with a unit supervisor or the Sacramento County DCFAS Ombudsperson (Tracy Trinh) to independently evaluate the facts of this case before any further voluntary agreements are drafted.

I request that this statement be placed permanently into my department file. I look forward to resolving this matter transparently, factually, and swiftly so that I may be reunited with my sons.

Sincerely,

{full_name}
Phone: {phone_num}
"""

    filename = "CPS_Formal_Statement.txt"
    
    try:
        with open(filename, "w") as file:
            file.write(document_content)
        
        print("\n" + "="*40)
        print("[SUCCESS] Your personalized birthday statement has been compiled!")
        print(f"Saved to local directory as: {filename}")
        print("="*40)
        print("\nTo view and copy the text directly in Termux, run:")
        print(f"cat {filename}")
        print("\nTo read it line-by-line, run:")
        print(f"less {filename}")
    except Exception as e:
        print(f"\n[ERROR] Could not write file to storage: {e}")

if __name__ == "__main__":
    generate_cps_document()

