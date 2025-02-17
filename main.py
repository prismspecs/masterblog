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


@app.route("/like/<int:post_id>")
def like(post_id):
    """Increment likes for a blog post."""
    blog_posts = load_blog_posts()
    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1  # Increment likes
            break

    save_blog_posts(blog_posts)
    return redirect(url_for("index"))


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
            new_post = {"id": new_id, "author": author, "title": title, "content": content, "likes": 0}
            blog_posts.append(new_post)
            save_blog_posts(blog_posts)

            return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Handle updating a blog post."""
    blog_posts = load_blog_posts()
    post = next((p for p in blog_posts if p["id"] == post_id), None)

    if not post:
        return "Post not found", 404

    if request.method == "POST":
        post["author"] = request.form.get("author")
        post["title"] = request.form.get("title")
        post["content"] = request.form.get("content")

        save_blog_posts(blog_posts)
        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Delete a blog post by ID and redirect to home page."""
    blog_posts = load_blog_posts()
    blog_posts = [post for post in blog_posts if post["id"] != post_id]  # Remove post with matching ID
    save_blog_posts(blog_posts)

    return redirect(url_for("index"))


@app.route("/api/posts")
def api_posts():
    """Return blog posts as JSON (optional API endpoint for debugging)."""
    return jsonify(load_blog_posts())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
