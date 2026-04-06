# Blog System - Quick Testing Guide

## 1. Create Test Data

Open Django shell:
```bash
python manage.py shell
```

Then run:
```python
from core.models import Blog

# Create multiple test blogs
blogs = [
    {
        'title': 'Advances in Medical Technology: What Students Should Know',
        'body': 'The landscape of medical technology has undergone a revolutionary transformation over the past decade. From artificial intelligence-powered diagnostic tools to cutting-edge surgical robots, the intersection of technology and medicine continues to reshape healthcare delivery.',
        'author': 'Dr. Sarah Johnson',
        'category': 'research'
    },
    {
        'title': 'Telemedicine: The Future of Patient Care',
        'body': 'Explore how telemedicine is revolutionizing patient care and making healthcare more accessible to remote communities. The COVID-19 pandemic accelerated the adoption of telemedicine, but the benefits extend far beyond emergency response.',
        'author': 'Dr. Michael Chen',
        'category': 'healthTech'
    },
    {
        'title': 'Study Tips for Medical Exams',
        'body': 'Proven strategies and techniques to help medical students ace their exams and improve retention of complex medical concepts. Success in medical education requires more than just memorization.',
        'author': 'Dr. Emma Williams',
        'category': 'education'
    },
    {
        'title': 'Work-Life Balance in Medicine',
        'body': 'Learn how to maintain a healthy work-life balance while pursuing a demanding career in medicine and healthcare. Burnout is a serious concern in medical practice.',
        'author': 'Dr. James Smith',
        'category': 'lifestyle'
    },
    {
        'title': 'Breakthrough in Cancer Research',
        'body': 'Discover recent breakthroughs in cancer research and their implications for treatment methods and patient outcomes. New immunotherapy approaches are showing promise.',
        'author': 'Dr. Lisa Anderson',
        'category': 'science'
    },
    {
        'title': 'Financial Planning for Medical Students',
        'body': 'Smart financial strategies for managing student loans and building a strong financial foundation during medical school. Understanding finances early is crucial for long-term success.',
        'author': 'Dr. Robert Davis',
        'category': 'finance'
    },
]

for blog_data in blogs:
    Blog.objects.create(**blog_data)

print("✅ Created 6 test blogs!")
```

Exit shell:
```python
exit()
```

## 2. Test Blog List View

**URL**: http://localhost:8000/blogs/

**Expected Features**:
- ✅ Hero section with title "Blog"
- ✅ Featured blog card (latest blog)
- ✅ Category filter dropdown
- ✅ Grid of 6 blog cards (or fewer if less blogs created)
- ✅ Each card shows: title, image, author, date, category
- ✅ Pagination controls (if more than 6 blogs)
- ✅ Newsletter signup form

## 3. Test Category Filtering

**URLs to test**:
- http://localhost:8000/blogs/?category=research
- http://localhost:8000/blogs/?category=healthTech
- http://localhost:8000/blogs/?category=education
- http://localhost:8000/blogs/?category=lifestyle
- http://localhost:8000/blogs/?category=science
- http://localhost:8000/blogs/?category=finance

**Expected**: Only blogs with selected category should display

## 4. Test Blog Detail View

**URL**: http://localhost:8000/blogs/1/

**Expected Features**:
- ✅ Large hero header with blog image
- ✅ Blog title and metadata
- ✅ Author information with avatar
- ✅ Full blog content with formatting
- ✅ Share buttons (Facebook, Twitter, Email, Copy Link)
- ✅ Author bio box
- ✅ Related articles section (if available)
- ✅ Newsletter CTA
- ✅ Back to blogs button

## 5. Test Pagination

1. Create more than 6 blogs
2. Visit http://localhost:8000/blogs/
3. Verify:
   - ✅ First 6 blogs displayed
   - ✅ "Next" button appears
   - ✅ Page numbers shown
   - ✅ Clicking page numbers works

## 6. Test Related Articles

1. Visit a blog detail page (e.g., http://localhost:8000/blogs/1/)
2. Scroll to "Related Articles" section
3. Verify:
   - ✅ Up to 2 related blogs from same category display
   - ✅ They link to their detail pages
   - ✅ They show category, title, and date

## 7. Test Responsive Design

Check the blog pages on:
- ✅ Desktop (full width)
- ✅ Tablet (medium width)
- ✅ Mobile (small width)

All elements should reflow properly.

## 8. Test Images

1. Upload an image to a blog via Django admin
2. Visit blog list page
3. Verify image displays properly
4. Visit blog detail page
5. Verify image displays in hero section

## 9. Test Links

Verify these links work:
- ✅ Blog card → Blog detail page
- ✅ Category filter → Filtered list
- ✅ Pagination numbers → Correct page
- ✅ Featured blog → Blog detail
- ✅ Related articles → Blog detail
- ✅ Back to blogs button → Blog list
- ✅ Home navigation → Home page

## 10. Common Issues & Fixes

### Issue: "Page not found" on blog URLs
**Fix**: Make sure you've migrated and created test data

### Issue: Images not showing
**Fix**: 
- Check `MEDIA_ROOT` and `MEDIA_URL` in settings
- Ensure images are uploaded to correct folder

### Issue: Category filter shows no results
**Fix**: 
- Verify blog has correct category value
- Check filter parameter spelling

### Issue: Related articles not showing
**Fix**: 
- Create multiple blogs with same category
- Related blogs exclude current blog automatically

## Django Admin

You can also manage blogs via Django admin:

1. Run: `python manage.py runserver`
2. Go to: http://localhost:8000/admin/
3. Log in with superuser credentials
4. Under "Core" section, click "Blogs"
5. Create/Edit/Delete blogs as needed

## Database Queries

The views are optimized with:
- Ordered by `-created_at` (newest first)
- Paginated to 6 per page
- Category filtering available
- Related blogs query excludes current blog

---

**Ready to test!** 🚀

If you encounter any issues, check:
1. Migrations are applied
2. Test data is created
3. All URLs are correct
4. Templates are in correct directories
