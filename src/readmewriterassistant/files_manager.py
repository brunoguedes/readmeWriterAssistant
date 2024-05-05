import os

class FilesManager:
    def list_files(self, base_path="./", exclude=None):
        if exclude is None:
            exclude = []

        result = []

        for root, dirs, files in os.walk(base_path):
            dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__" and d not in exclude]

            filtered_items = [item for item in files if not any(ignore in item for ignore in [".DS_Store", ".gitignore"])]
            for file in filtered_items:
                if file not in exclude:
                    relative_path = os.path.relpath(os.path.join(root, file), base_path)
                    result.append(relative_path)

            for dir in dirs:
                if dir not in exclude:
                    relative_path = os.path.relpath(os.path.join(root, dir), base_path) + "/"
                    result.append(relative_path)

        return sorted(result)

    def format_file_tree(self, file_list):
        tree = {}
        for path in file_list:
            parts = path.split("/")
            current = tree
            for part in parts:
                if part != "":
                    if part not in current:
                        current[part] = {}
                    current = current[part]

        def print_tree(node, prefix="", is_last=True):
            tree_structure = ""
            if isinstance(node, dict):
                keys = list(node.keys())
                for i, key in enumerate(keys):
                    is_last_child = i == len(keys) - 1
                    tree_structure += prefix + ("└── " if is_last_child else "├── ") + key + "\n"
                    tree_structure += print_tree(node[key], prefix + ("    " if is_last_child else "│   "), is_last_child)
            return tree_structure

        return print_tree(tree).strip()
    
    def read_file_content(self, base_path, file):
        file_path = os.path.join(base_path, file)
        content = ""
        if os.path.isfile(file_path):
            content += f"## {file}:\n\n```\n"
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                content += file.read()
            content += "\n```\n\n"
        return content.strip()

    def read_files_content(self, base_path, items):
        content = ""
        for item in items:
            item_path = os.path.join(base_path, item)
            if os.path.isfile(item_path):
                content += self.read_file_content(base_path, item)
            # elif os.path.isdir(item_path):
            #     for root, dirs, files in os.walk(item_path):
            #         for file in files:
            #             file_path = os.path.relpath(os.path.join(root, file), base_path)
            #             content += self.read_file_content(base_path, file_path)
        return content.strip()
