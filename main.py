import uuid
from typing import Optional, Any

from langchain_core.messages import HumanMessage

from src.graph.workflow import create_workflow


class ChatApp:
    def __init__(self):
        self.workflow = create_workflow()
        self.config = {"configurable": {"thread_id": str(uuid.uuid4())}}
        self.cached_responses = ["hi!", "rag prompt", "1 rag, 2 none, 3 no, 4 no", "red", "q"]
        self.cached_index = 0

    def get_user_input(self) -> Optional[str]:
        try:
            return input("User (q/Q to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            return "q"
        except:
            if self.cached_index < len(self.cached_responses):
                response = self.cached_responses[self.cached_index]
                self.cached_index += 1
                print(f"User (q/Q to quit): {response}")
                return response
            return "q"

    def process_message(self, user_input: str) -> None:
        for output in self.workflow.stream({"messages": [HumanMessage(content=user_input)]}, config=self.config, stream_mode="updates"):
            self.display_response(output)

    def display_response(self, output: dict[str, Any]) -> None:
        last_message = next(iter(output.values()))["messages"][-1]
        last_message.pretty_print()

    def run(self) -> None:
        print("Prompt Generator Chat - Type 'q' to quit\n")
        while True:
            user_input = self.get_user_input()

            if not user_input or user_input.lower() in {"q", "quit"}:
                print("AI: Goodbye!")
                break

            self.process_message(user_input)


def main() -> None:
    app = ChatApp()
    app.run()


if __name__ == "__main__":
    main()
