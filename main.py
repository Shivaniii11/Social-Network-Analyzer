from colorama import Fore, init
init(autoreset=True)

from models import add_user, add_connection, get_users, get_connections, get_user_name
from graph_logic import build_graph, mutual_connections, shortest_path, most_connected
from recommendations import recommend_connections
from visualize import visualize_graph
from utils import menu


def main():
    print(Fore.YELLOW + "⚠ Make sure you ran schema.sql in MySQL first!")

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_user(input("Name: "), input("Email: "))

        elif choice == '2':
            add_connection(int(input("User 1 ID: ")), int(input("User 2 ID: ")))

        elif choice == '3':
            print(Fore.CYAN + "\n--- Users ---")
            for u in get_users():
                print(f"ID:{u[0]} | {u[1]} | {u[2]}")

        elif choice == '4':
            graph = build_graph(get_connections())
            mutual = mutual_connections(graph, int(input("User1: ")), int(input("User2: ")))

            print(Fore.CYAN + "\nMutual Connections:")
            for m in mutual:
                print(Fore.GREEN + get_user_name(m))

        elif choice == '5':
            graph = build_graph(get_connections())
            path = shortest_path(graph, int(input("Start: ")), int(input("End: ")))

            print(Fore.CYAN + "\nPath:")
            if path:
                print(" → ".join(get_user_name(i) for i in path))
            else:
                print(Fore.RED + "No path found")

        elif choice == '6':
            graph = build_graph(get_connections())
            recs = recommend_connections(graph, int(input("User ID: ")))

            print(Fore.CYAN + "\nRecommendations:")
            for u, score in recs:
                print(Fore.GREEN + f"{get_user_name(u)} ({score} mutual)")

        elif choice == '7':
            graph = build_graph(get_connections())
            u, conns = most_connected(graph)
            print(Fore.GREEN + f"{get_user_name(u)} has {len(conns)} connections")

        elif choice == '8':
            print(Fore.CYAN + "Opening graph...")
            visualize_graph()

        elif choice == '0':
            break

        else:
            print(Fore.RED + "Invalid choice")


if __name__ == "__main__":
    main()