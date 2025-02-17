from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Define the path to the JSON file
BLOG_FILE = "blog_posts.json"


def load_blog_posts():
    """Load blog posts from the JSON file."""
    if not os.path.exists(BLOG_FILE):
        return []  # Return an empty list if the file doesn't exist

    with open(BLOG_FILE, "r") as file:
        try:
            return json.load(file)  # Load and return the blog posts
        except json.JSONDecodeError:
            return []  # Return an empty list if JSON is invalid


def save_blog_posts(posts):
    """Save blog posts to the JSON file."""
    with open(BLOG_FILE, "w") as file:
        json.dump(posts, file, indent=4)


@app.route("/")
def index():
    """Render the homepage with blog posts loaded from the JSON file."""
    blog_posts = load_blog_posts()
    return render_template("index.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Handle adding a new blog post."""
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        if author and title and content:  # Ensure all fields are filled
            blog_posts = load_blog_posts()
            new_id = max([post["id"] for post in blog_posts], default=0) + 1  # Generate a unique ID
            new_post = {"id": new_id, "author": author, "title": title, "content": content}
            blog_posts.append(new_post)
            save_blog_posts(blog_posts)

            return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/api/posts")
def api_posts():
    """Return blog posts as JSON (optional API endpoint for debugging)."""
    return jsonify(load_blog_posts())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
