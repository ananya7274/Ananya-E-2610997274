books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach",
     "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {book[3] for book in books}
student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}

while True:   
    print("\n" + "=" * 50)
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 50)

    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")

        for i, (title, author, year, category) in enumerate(books, start=1):
            print(
                f'{i}. "{title}" by {author} ({year}) '
                f'| Genre: {category}'
            )

        print(f"Total Books: {len(books)}")
    elif choice == "2":
        print("\n--- Add New Book Record ---")

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if title and author and year and category:
            # Store new record as an immutable tuple
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)

            print(
                f'\n[SUCCESS] "{title}" added as an '
                "immutable catalog record."
            )
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All book details are required.")
    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")

        for category in sorted(library_categories):
            print(f"- {category}")

        print(f"Total Unique Genres: {len(library_categories)}")
    elif choice == "4":
        category = input(
            "Enter a category to add to the student wishlist: "
        ).strip()

        if category:
            student_wishlist.add(category)
            print(
                f'[SUCCESS] "{category}" added to student wishlist.'
            )
        else:
            print("[ERROR] Category cannot be empty.")
    elif choice == "5":
        print("\n--- Category Gap Analysis ---")
        missing_categories = student_wishlist - library_categories
        common_categories = student_wishlist & library_categories
        all_categories = student_wishlist | library_categories

        print("\nWishlist Categories Missing from Library:")
        if missing_categories:
            for category in sorted(missing_categories):
                print(f"- {category}")
        else:
            print("None")

        print("\nCategories Available in Both:")
        if common_categories:
            for category in sorted(common_categories):
                print(f"- {category}")
        else:
            print("None")

        print("\nAll Categories (Library + Wishlist):")
        for category in sorted(all_categories):
            print(f"- {category}")

        print(f"\nMissing Categories Count: {len(missing_categories)}")
    elif choice == "6":
        print("\nThank you for using the Library Book & Category Manager!")
        break
    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 6.")
