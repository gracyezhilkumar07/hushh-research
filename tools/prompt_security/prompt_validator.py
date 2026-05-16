from injection_detector import detect_prompt_injection


def main():

    user_prompt = input("Enter prompt to validate:\n")

    findings = detect_prompt_injection(user_prompt)

    if findings:

        print("\nRisk Level: HIGH")
        print("Detected Issues:\n")

        for finding in findings:
            print(f"- {finding}")

    else:
        print("\nPrompt appears safe.")


if __name__ == "__main__":
    main()