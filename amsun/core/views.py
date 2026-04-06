from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, News, Events

class HomeView(TemplateView):
    template_name = 'core/home.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'core/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the featured blog (latest one)
        context['featured_blog'] = Blog.objects.first()
        # Get all unique categories for the filter
        context['categories'] = Blog.CATEGORY_CHOICES
        return context
    
    def get_queryset(self):
        queryset = Blog.objects.all().order_by('-created_at')
        category = self.request.GET.get('category')
        
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'core/blog_detail.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related blogs from the same category (exclude current blog)
        current_blog = self.get_object()
        context['related_blogs'] = Blog.objects.filter(
            category=current_blog.category
        ).exclude(pk=current_blog.pk)[:2]
        return context


class NewsListView(ListView):
    model = News
    template_name = 'core/news.html'
    context_object_name = 'news'
    paginate_by = 12
    ordering = ['-published_date']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the featured news (latest one)
        context['featured_news'] = News.objects.first()
        # Get all unique categories for the filter
        context['categories'] = News.CATEGORY_CHOICES
        # Get trending news (latest 3)
        context['trending_news'] = News.objects.all()[:3]
        return context
    
    def get_queryset(self):
        queryset = News.objects.all().order_by('-published_date')
        category = self.request.GET.get('category')
        
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset


class EventsListView(ListView):
    model = Events
    template_name = 'core/events.html'
    context_object_name = 'events'
    paginate_by = 12
    ordering = ['-date']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the featured event (latest one)
        context['featured_event'] = Events.objects.first()
        # Get all unique categories for the filter
        context['categories'] = Events.CATEGORY_CHOICES
        # Get upcoming events (latest 5)
        context['upcoming_events'] = Events.objects.all().order_by('date')[:5]
        return context
    
    def get_queryset(self):
        queryset = Events.objects.all().order_by('-date')
        category = self.request.GET.get('category')
        
        if category:
            queryset = queryset.filter(category=category)
        
        return queryset


class ConferenceView(TemplateView):
    template_name = 'core/conference.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conference_year'] = 2025
        context['conference_date'] = 'May 15-17, 2025'
        return context


class AlumniView(TemplateView):
    template_name = 'core/alumni.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Alumni Statistics
        context['alumni_stats'] = {
            'total_alumni': '15,000+',
            'global_countries': '85+',
            'active_members': '8,500+',
            'recent_graduates': '2024-2025',
        }
        
        # Featured Alumni Stories
        context['featured_alumni'] = [
            {
                'name': 'Dr. James Kipchoge',
                'class_year': '2010',
                'position': 'Chief Medical Officer, East African Health Initiative',
                'bio': 'Leading healthcare innovation across East Africa with focus on rural health delivery',
                'image': 'https://via.placeholder.com/400x500?text=Dr.+James+Kipchoge',
                'specialty': 'Public Health Leadership',
            },
            {
                'name': 'Prof. Sarah Mwangi',
                'class_year': '2008',
                'position': 'Head of Cardiology Department, KNH',
                'bio': 'Pioneering cardiac research and mentoring the next generation of cardiologists',
                'image': 'https://via.placeholder.com/400x500?text=Prof.+Sarah+Mwangi',
                'specialty': 'Clinical Excellence',
            },
            {
                'name': 'Dr. Michael Ochieng',
                'class_year': '2015',
                'position': 'Founder & CEO, MediTech Solutions Kenya',
                'bio': 'Building innovative medical technology solutions transforming healthcare delivery',
                'image': 'https://via.placeholder.com/400x500?text=Dr.+Michael+Ochieng',
                'specialty': 'Healthcare Innovation',
            },
        ]
        
        # Alumni Chapters/Regions
        context['chapters'] = [
            {
                'name': 'Nairobi Chapter',
                'members': '3,200+',
                'location': 'Nairobi, Kenya',
                'icon': 'fas fa-city',
                'active': True,
            },
            {
                'name': 'East Africa Chapter',
                'members': '2,100+',
                'location': 'Kampala, Uganda & Dar es Salaam, Tanzania',
                'icon': 'fas fa-globe',
                'active': True,
            },
            {
                'name': 'Southern Africa Chapter',
                'members': '1,800+',
                'location': 'Johannesburg, South Africa',
                'icon': 'fas fa-map-pin',
                'active': True,
            },
            {
                'name': 'Europe & Americas Chapter',
                'members': '2,400+',
                'location': 'London, New York, Toronto',
                'icon': 'fas fa-globe',
                'active': True,
            },
            {
                'name': 'Asia-Pacific Chapter',
                'members': '1,600+',
                'location': 'Singapore, Dubai, Sydney',
                'icon': 'fas fa-plane',
                'active': True,
            },
        ]
        
        return context


class PartnersView(TemplateView):
    template_name = 'core/partners.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Partnership Stats
        context['partnership_stats'] = {
            'total_partners': '150+',
            'annual_investment': 'KES 500M+',
            'students_impacted': '5,000+',
            'programs_delivered': '200+',
        }
        
        # Sponsorship Tiers
        context['sponsorship_tiers'] = [
            {
                'name': 'Platinum Partner',
                'price': 'KES 5,000,000+',
                'color': 'from-yellow-400 to-yellow-600',
                'benefits': [
                    'Exclusive naming rights to major conference or event',
                    'Prominent branding across all AMSUN platforms',
                    'Reserved seats at executive events (unlimited)',
                    'Dedicated partnership manager',
                    'Customized research collaboration opportunities',
                    'First access to innovative programs',
                    'Media coverage and press releases',
                    'Annual impact report highlighting partnership',
                    'Logo on AMSUN merchandise and materials',
                    'VIP reception and gala attendance',
                ],
                'highlight': True,
            },
            {
                'name': 'Gold Partner',
                'price': 'KES 2,500,000 - 4,999,999',
                'color': 'from-orange-400 to-orange-600',
                'benefits': [
                    'Prominent branding on website and materials',
                    'Reserved seats at 4 major events per year',
                    'Partnership manager contact',
                    'Co-branded marketing materials',
                    'Recognition in newsletter and social media',
                    'Educational partnership opportunities',
                    'Recruitment access to talented students',
                    'Annual report feature',
                    'Logo on select materials',
                    'Priority sponsorship renewal',
                ],
            },
            {
                'name': 'Silver Partner',
                'price': 'KES 1,000,000 - 2,499,999',
                'color': 'from-gray-300 to-gray-500',
                'benefits': [
                    'Branding on AMSUN website',
                    'Reserved seats at 2 major events per year',
                    'Recognition in quarterly newsletter',
                    'Social media mentions and highlights',
                    'Intern recruitment opportunities',
                    'Event sponsorship opportunities',
                    'Co-marketing initiatives',
                    'Annual recognition plaque',
                    'Access to student database',
                ],
            },
            {
                'name': 'Bronze Partner',
                'price': 'KES 250,000 - 999,999',
                'color': 'from-amber-600 to-orange-700',
                'benefits': [
                    'Partner logo on website',
                    'Event sponsorship options',
                    'Social media recognition',
                    'Newsletter mentions',
                    'Recruitment access',
                    'Certificate of partnership',
                    'Annual report inclusion',
                ],
            },
        ]
        
        # Success Stories / Case Studies
        context['case_studies'] = [
            {
                'company': 'Nairobi Pharma Group',
                'logo': 'https://via.placeholder.com/200?text=Pharma+Group',
                'challenge': 'Need to identify and nurture healthcare innovation talent',
                'solution': 'Partnered with AMSUN for internship program and research collaboration',
                'results': 'Hired 12 top performers, conducted 3 joint research projects',
                'investment': 'KES 3.5M annually',
                'quote': 'AMSUN partnership gave us access to exceptional talent and fresh perspectives in healthcare innovation',
                'executive': 'Dr. Margaret Kipchoge, CEO',
            },
            {
                'company': 'East Africa Healthcare Solutions',
                'logo': 'https://via.placeholder.com/200?text=Healthcare+Solutions',
                'challenge': 'Building brand awareness among medical students',
                'solution': 'Sponsored AMSUN Scientific Conference and student workshops',
                'results': '2,500+ student engagements, 15% recruitment increase',
                'investment': 'KES 2.8M annually',
                'quote': 'Investing in AMSUN gives us direct access to Africa\'s future healthcare leaders',
                'executive': 'James Kiplagat, Business Development Director',
            },
            {
                'company': 'Innovation Labs Africa',
                'logo': 'https://via.placeholder.com/200?text=Innovation+Labs',
                'challenge': 'Finding startup mentors and advisors for healthcare projects',
                'solution': 'Created AMSUN Entrepreneurship Accelerator program',
                'results': '8 successful healthcare startups incubated, 200+ students mentored',
                'investment': 'KES 4.2M annually',
                'quote': 'This partnership is transforming how we nurture medical entrepreneurship in Africa',
                'executive': 'Priya Patel, Program Director',
            },
        ]
        
        # Current Partners/Clients
        context['current_partners'] = [
            'Nairobi Pharma',
            'KNH',
            'Roche',
            'Pfizer',
            'GSK',
            'AMREF',
            'MSF',
            'WHO',
            'Red Cross',
            'Lioncrest',
            'Equity Bank',
            'Standard Chartered',
        ]
        
        return context


class LeadershipView(TemplateView):
    template_name = 'core/leadership.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Patron
        context['patron'] = {
            'name': 'Prof. Peter Kiprotich Koech',
            'bio': 'Distinguished medical educator with over 30 years of experience in medical education and student development. Committed to fostering excellence in the medical profession.',
            'email': 'p.koech@uonbi.ac.ke',
            'image': 'https://via.placeholder.com/300?text=Patron'
        }
        
        # Executive Committee
        context['executive'] = [
            {
                'name': 'Sarah Kipchoge',
                'role': 'chairperson',
                'bio': 'Final year medical student with a passion for student welfare and advocacy.',
                'email': 'sarah.kipchoge@amsun.ac.ke',
                'phone': '+254 712 345 678',
                'image': 'https://via.placeholder.com/300?text=Chairperson'
            },
            {
                'name': 'Michael Mwangi',
                'role': 'vice_chairperson',
                'bio': 'Dedicated to fostering unity and coordination within AMSUN.',
                'email': 'michael.mwangi@amsun.ac.ke',
                'phone': '+254 712 345 679',
                'image': 'https://via.placeholder.com/300?text=Vice+Chair'
            },
            {
                'name': 'Grace Njoroge',
                'role': 'secretary',
                'bio': 'Ensuring effective communication and documentation of AMSUN activities.',
                'email': 'grace.njoroge@amsun.ac.ke',
                'phone': '+254 712 345 680',
                'image': 'https://via.placeholder.com/300?text=Secretary'
            },
            {
                'name': 'David Kiplagat',
                'role': 'treasurer',
                'bio': 'Managing resources responsibly to support AMSUN initiatives.',
                'email': 'david.kiplagat@amsun.ac.ke',
                'phone': '+254 712 345 681',
                'image': 'https://via.placeholder.com/300?text=Treasurer'
            },
            {
                'name': 'Jane Wanjiru',
                'role': 'academic_affairs',
                'bio': 'Championing academic excellence and student learning outcomes.',
                'email': 'jane.wanjiru@amsun.ac.ke',
                'phone': '+254 712 345 682',
                'image': 'https://via.placeholder.com/300?text=Academic+Officer'
            },
            {
                'name': 'Emmanuel Kipchoge',
                'role': 'welfare_officer',
                'bio': 'Advocating for student welfare and mental health support.',
                'email': 'emmanuel.kipchoge@amsun.ac.ke',
                'phone': '+254 712 345 683',
                'image': 'https://via.placeholder.com/300?text=Welfare+Officer'
            },
            {
                'name': 'Alex Musa',
                'role': 'sports_officer',
                'bio': 'Promoting fitness, teamwork, and sports excellence among students.',
                'email': 'alex.musa@amsun.ac.ke',
                'phone': '+254 712 345 684',
                'image': 'https://via.placeholder.com/300?text=Sports+Officer'
            },
            {
                'name': 'Beatrice Kamau',
                'role': 'cultural_officer',
                'bio': 'Celebrating diversity and promoting cultural heritage within AMSUN.',
                'email': 'beatrice.kamau@amsun.ac.ke',
                'phone': '+254 712 345 685',
                'image': 'https://via.placeholder.com/300?text=Cultural+Officer'
            },
        ]
        
        # Class Representatives
        context['class_reps'] = [
            {
                'name': 'Kariuki Samuel',
                'class_year': 'Year 1',
                'bio': 'First year representative ensuring smooth integration and support for new students.',
                'email': 'kariuki.samuel@amsun.ac.ke',
                'phone': '+254 712 345 700'
            },
            {
                'name': 'Amara Ochieng',
                'class_year': 'Year 2',
                'bio': 'Bridge between first and third year students, fostering mentorship.',
                'email': 'amara.ochieng@amsun.ac.ke',
                'phone': '+254 712 345 701'
            },
            {
                'name': 'Liam Kipchoge',
                'class_year': 'Year 3',
                'bio': 'Transitioning to clinical years, supporting clinical student concerns.',
                'email': 'liam.kipchoge@amsun.ac.ke',
                'phone': '+254 712 345 702'
            },
            {
                'name': 'Zara Mutua',
                'class_year': 'Year 4',
                'bio': 'Clinical year representative addressing healthcare practice challenges.',
                'email': 'zara.mutua@amsun.ac.ke',
                'phone': '+254 712 345 703'
            },
            {
                'name': 'Okech Daniel',
                'class_year': 'Year 5',
                'bio': 'Senior clinical student mentoring juniors and leading clinical initiatives.',
                'email': 'okech.daniel@amsun.ac.ke',
                'phone': '+254 712 345 704'
            },
            {
                'name': 'Monica Adeyemi',
                'class_year': 'Year 6',
                'bio': 'Final year representative guiding students through graduation and career preparation.',
                'email': 'monica.adeyemi@amsun.ac.ke',
                'phone': '+254 712 345 705'
            },
        ]
        
        # Advisory Board
        context['advisory_board'] = [
            {
                'name': 'Dr. Jane Wambua',
                'bio': 'Senior Lecturer in Internal Medicine with expertise in student mentorship programs.',
                'email': 'j.wambua@uonbi.ac.ke',
                'phone': '+254 712 999 001'
            },
            {
                'name': 'Prof. Isaac Kiplagat',
                'bio': 'Dean of Medicine overseeing academic standards and institutional development.',
                'email': 'i.kiplagat@uonbi.ac.ke',
                'phone': '+254 712 999 002'
            },
            {
                'name': 'Dr. Susan Mutua',
                'bio': 'Director of Student Affairs ensuring student wellbeing and support services.',
                'email': 's.mutua@uonbi.ac.ke',
                'phone': '+254 712 999 003'
            },
            {
                'name': 'Prof. James Ochieng',
                'bio': 'Medical Education Expert advocating for curriculum innovation and excellence.',
                'email': 'j.ochieng@uonbi.ac.ke',
                'phone': '+254 712 999 004'
            },
            {
                'name': 'Dr. Amina Hassan',
                'bio': 'Consultant Physician and advocate for public health and community engagement.',
                'email': 'a.hassan@uonbi.ac.ke',
                'phone': '+254 712 999 005'
            },
            {
                'name': 'Mr. Patrick Kipchoge',
                'bio': 'Alumni representative bridging institutional and professional community interests.',
                'email': 'p.kipchoge@amsunalumni.ac.ke',
                'phone': '+254 712 999 006'
            },
        ]
        
        # Previous Chairpersons
        context['previous_chairpersons'] = [
            {
                'name': 'Dr. Ruth Kamau',
                'term_year': '2024-2025',
                'bio': 'Pioneered student wellness initiatives and campus development projects.',
                'image': 'https://via.placeholder.com/300?text=Ruth+Kamau'
            },
            {
                'name': 'Mr. Kwame Asante',
                'term_year': '2023-2024',
                'bio': 'Led major advocacy campaigns for improved medical education infrastructure.',
                'image': 'https://via.placeholder.com/300?text=Kwame+Asante'
            },
            {
                'name': 'Ms. Priya Patel',
                'term_year': '2022-2023',
                'bio': 'Strengthened AMSUN-industry partnerships and internship opportunities.',
                'image': 'https://via.placeholder.com/300?text=Priya+Patel'
            },
            {
                'name': 'Mr. Thomas Kipchoge',
                'term_year': '2021-2022',
                'bio': 'Established mentorship program connecting students with medical professionals.',
                'image': 'https://via.placeholder.com/300?text=Thomas+Kipchoge'
            },
            {
                'name': 'Dr. Amelia Osei',
                'term_year': '2020-2021',
                'bio': 'Launched digital transformation initiatives and online learning platforms.',
                'image': 'https://via.placeholder.com/300?text=Amelia+Osei'
            },
        ]
        
        return context

