(function () {
  const container = document.getElementById("blog-list");
  const emptyState = document.getElementById("blog-empty");

  if (!container) {
    return;
  }

  function formatDate(isoString) {
    const date = new Date(isoString);
    if (Number.isNaN(date.getTime())) {
      return "Date non définie";
    }
    return new Intl.DateTimeFormat("fr-BE", {
      day: "2-digit",
      month: "long",
      year: "numeric"
    }).format(date);
  }

  function render(posts) {
    container.innerHTML = "";

    if (!posts.length) {
      if (emptyState) {
        emptyState.hidden = false;
      }
      return;
    }

    if (emptyState) {
      emptyState.hidden = true;
    }

    for (const post of posts) {
      const card = document.createElement("article");
      card.className = "card blog-card";

      const meta = document.createElement("p");
      meta.className = "blog-meta";
      meta.textContent = "Publié le " + formatDate(post.publish_at);

      const title = document.createElement("h3");
      title.textContent = post.title || "Article";

      const summary = document.createElement("p");
      summary.textContent = post.summary || "";

      const link = document.createElement("a");
      link.className = "blog-link";
      link.href = post.url || "#";
      link.textContent = "Lire l'article";

      card.appendChild(meta);
      card.appendChild(title);
      card.appendChild(summary);
      card.appendChild(link);
      container.appendChild(card);
    }
  }

  async function loadPosts() {
    try {
      const res = await fetch("data/posts.json", { cache: "no-store" });
      if (!res.ok) {
        throw new Error("Impossible de charger les actualités");
      }
      const data = await res.json();
      const allPosts = Array.isArray(data.posts) ? data.posts : [];
      const now = new Date();

      const visiblePosts = allPosts
        .filter(function (post) {
          const d = new Date(post.publish_at);
          return !Number.isNaN(d.getTime()) && d <= now;
        })
        .sort(function (a, b) {
          return new Date(b.publish_at) - new Date(a.publish_at);
        });

      render(visiblePosts);
    } catch (error) {
      console.error(error);
      if (emptyState) {
        emptyState.hidden = false;
        emptyState.textContent = "Impossible de charger les actualités pour le moment.";
      }
    }
  }

  loadPosts();
})();
