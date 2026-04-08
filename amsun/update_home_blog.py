from pathlib import Path
path = Path('core/templates/core/home.html')
text = path.read_text(encoding='utf-8')
start = '<section class="py-8 md:py-12 bg-white'>\n'
end = '\n<section class="py-16 bg-amsun-gray overflow-hidden">'
if start not in text or end not in text:
    raise SystemExit('Markers not found in home.html')
pre, rest = text.split(start, 1)
mid, post = rest.split(end, 1)
new_mid = '''<section class="py-8 md:py-12 bg-white">
    <div class="container mx-auto px-4 max-w-7xl">
        <div class="flex justify-between items-end mb-8 md:mb-10">
            <div>
                <span class="text-amsun-red font-bold tracking-widest uppercase text-[10px] md:text-xs mb-1 block">Insights</span>
                <h2 class="text-2xl md:text-3xl font-display font-bold text-gray-900">Latest from the Blog</h2>
            </div>
            <a href="{% url 'blog-list' %}" class="inline-flex items-center gap-1.5 text-[10px] md:text-xs font-bold text-amsun-red hover:text-amsun-black transition-colors group">
                Read All Articles
                <span class="w-6 h-6 rounded-full bg-amsun-red/10 flex items-center justify-center group-hover:bg-amsun-red group-hover:text-white transition-all">
                    <i class="fas fa-arrow-right text-[10px]"></i>
                </span>
            </a>
        </div>

        {% if blog_posts %}
        <div class="grid grid-cols-1 lg:grid-cols-4 gap-4 md:gap-5">
            {% with featured=blog_posts.0 %}
            <div class="lg:col-span-2 relative rounded-[5px] overflow-hidden h-[280px] md:h-[320px] group cursor-pointer shadow-lg hover:shadow-xl transition-all duration-500 border border-gray-200">
                <img src="{% if featured.image %}{{ featured.image.url }}{% else %}https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80{% endif %}" class="w-full h-full object-cover transition duration-700 group-hover:scale-105">
                <div class="absolute inset-0 bg-gradient-to-t from-gray-900/95 via-gray-900/50 to-transparent flex flex-col justify-end p-5 md:p-6">
                    <span class="text-[9px] text-amsun-red bg-white px-2.5 py-1 rounded-[5px] w-max mb-3 font-bold uppercase tracking-wide shadow-sm">Featured</span>
                    <h3 class="text-white text-xl md:text-2xl font-bold mb-2 group-hover:text-amsun-gold transition-colors duration-300 leading-tight">{{ featured.title }}</h3>
                    <p class="text-gray-300 text-[11px] md:text-xs mb-4 line-clamp-2">{{ featured.body|striptags|truncatewords:20 }}</p>
                    <div class="flex items-center gap-4 text-[10px] md:text-xs text-gray-300 border-t border-gray-600/50 pt-3 w-full">
                        <span class="flex items-center gap-1.5 text-white font-medium"><i class="far fa-user-circle text-amsun-gold"></i> {{ featured.author }}</span>
                        <span class="flex items-center gap-1.5"><i class="far fa-clock"></i> 6 min read</span>
                        <span class="flex items-center gap-1.5 ml-auto"><i class="far fa-eye"></i> New</span>
                    </div>
                </div>
            </div>
            {% endwith %}

            <div class="flex flex-col divide-y divide-gray-200 border border-gray-100 rounded-[5px] overflow-hidden h-full">
                {% for post in blog_posts|slice:\"1:3\" %}
                <a href="{% url 'blog-detail' post.pk %}" class="p-3 md:p-4 hover:bg-gray-50 transition flex-grow flex flex-col justify-center">
                    <span class="text-[9px] md:text-[10px] uppercase text-amsun-red font-semibold">{{ post.get_category_display }}</span>
                    <h4 class="text-xs md:text-sm font-bold text-gray-900 mt-0.5 md:mt-1 leading-snug line-clamp-2">{{ post.title }}</h4>
                    <p class="text-[10px] md:text-xs text-gray-600 mt-0.5 md:mt-1 line-clamp-2">{{ post.body|striptags|truncatewords:15 }}</p>
                    <div class="flex items-center justify-between mt-1.5 md:mt-2 text-[10px] md:text-xs text-gray-500">
                        <span>By {{ post.author }}</span>
                        <span>{{ post.created_at|date:\"M d\" }}</span>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>

        <div class="mt-6 md:mt-8 grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
            {% for post in blog_posts|slice:\"3:6\" %}
            <a href="{% url 'blog-detail' post.pk %}" class="flex gap-3 md:gap-4 items-start group">
                <img src="{% if post.image %}{{ post.image.url }}{% else %}https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=400&q=80{% endif %}"
                    class="w-24 h-24 md:w-28 md:h-28 object-cover rounded-[5px] shrink-0 border border-gray-100">
                <div class="flex flex-col">
                    <h4 class="text-xs md:text-sm font-bold text-gray-900 group-hover:text-amsun-red transition leading-tight mb-1 line-clamp-2">{{ post.title }}</h4>
                    <p class="text-[10px] md:text-xs text-gray-600 line-clamp-2 mb-1">{{ post.body|striptags|truncatewords:20 }}</p>
                    <span class="text-[10px] md:text-xs text-gray-500">By {{ post.author }} • {{ post.created_at|date:\"M d, Y\" }}</span>
                </div>
            </a>
            {% endfor %}
        </div>
        {% else %}
        <div class="text-center py-12 text-gray-400">
            <i class="far fa-newspaper text-4xl mb-3 block"></i>
            <p class="font-medium">No blog posts available yet.</p>
        </div>
        {% endif %}
    </div>
</section>

<section class="py-16 bg-amsun-gray overflow-hidden">
'''
path.write_text(pre + new_mid + post, encoding='utf-8')
print('Updated home.html blog section')
