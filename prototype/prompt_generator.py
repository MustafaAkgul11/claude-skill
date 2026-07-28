def generate_prompt(role, task, context, constraints, output_format):
    prompt = f"""
<role>
{role}
</role>

<context>
{context}
</context>

<task>
{task}
</task>

<constraints>
{constraints}
</constraints>

<output_format>
{output_format}
</output_format>
"""
    return prompt.strip()


if __name__ == "__main__":
    print("=== Claude Prompt Generator ===\n")

    role = input("Role: ")
    task = input("Task: ")
    context = input("Context: ")
    constraints = input("Constraints: ")
    output_format = input("Output Format: ")

    print("\nGenerated Prompt\n")
    print(generate_prompt(role, task, context, constraints, output_format))
