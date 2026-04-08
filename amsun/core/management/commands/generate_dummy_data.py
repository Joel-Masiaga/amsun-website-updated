from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, time, timedelta
from core.models import News, Events, Blog, Research


class Command(BaseCommand):
    help = 'Generates dummy data for News, Events, Blog, and Research models'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        News.objects.all().delete()
        Events.objects.all().delete()
        Blog.objects.all().delete()
        Research.objects.all().delete()

        today = date.today()

        # ─── NEWS ─────────────────────────────────────────────────────────────────
        self.stdout.write('Creating News articles...')
        news_data = [
            {
                'headline': 'AMSUN Launches New Mental Health Support Program for Medical Students',
                'content': 'The Association of Medical Students of the University of Nairobi (AMSUN) has officially launched a comprehensive mental health support program aimed at addressing the growing concerns about burnout and stress among medical students. The program includes peer counselling, professional therapy sessions, and structured wellness workshops designed to help students manage the demanding nature of medical training. The initiative follows a survey that revealed over 60% of students experience significant academic stress during their studies.',
                'published_date': today - timedelta(days=1),
                'author': 'Dr. Amina Hassan',
                'category': 'announcement',
            },
            {
                'headline': 'UoN Medical Students Win East Africa Healthcare Innovation Award',
                'content': 'A team of AMSUN members has won the prestigious East Africa Healthcare Innovation Award for their mobile diagnostic application that enables community health workers to screen for malaria and tuberculosis in remote areas without laboratory access. The app uses machine learning algorithms trained on over 10,000 clinical cases from across the region. The team, led by fourth-year student James Kipchoge, presented their innovation at the annual East Africa Health Summit in Nairobi.',
                'published_date': today - timedelta(days=3),
                'author': 'Sarah Wanjiru',
                'category': 'achievement',
            },
            {
                'headline': 'New Academic Calendar Released: Key Changes for 2026 Academic Year',
                'content': 'The University of Nairobi School of Medicine has released the revised academic calendar for the 2026 academic year, incorporating several key changes including extended clinical rotation periods, new elective modules in digital health, and restructured examination schedules. AMSUN academic affairs secretary Jane Njoroge noted that the changes reflect a broader shift toward competency-based medical education. Students are advised to review the updated timetable on the official university portal.',
                'published_date': today - timedelta(days=5),
                'author': 'Kevin Oduya',
                'category': 'academic',
            },
            {
                'headline': 'AMSUN Partners with Kenyatta National Hospital for Expanded Clinical Placements',
                'content': 'AMSUN has signed a landmark partnership agreement with Kenyatta National Hospital (KNH) to expand clinical placement opportunities for medical students across all years of study. The partnership will provide structured mentorship from senior clinicians, access to specialized departments including oncology and neurosurgery, and opportunities to participate in ongoing clinical research projects. This partnership follows similar agreements with Aga Khan University Hospital and Nairobi Hospital.',
                'published_date': today - timedelta(days=7),
                'author': 'Grace Muthoni',
                'category': 'partnership',
            },
            {
                'headline': 'Groundbreaking Research on Malaria Drug Resistance Published by UoN Students',
                'content': 'Medical students affiliated with AMSUN have co-authored a groundbreaking research paper published in the Lancet Infectious Diseases journal, detailing new patterns of artemisinin resistance in malaria strains found in Western Kenya. The research, conducted in collaboration with KEMRI, involved blood sample analysis from over 1,200 patients across five counties. The findings have significant implications for national malaria treatment guidelines and are being reviewed by the Ministry of Health.',
                'published_date': today - timedelta(days=10),
                'author': 'Dr. Peter Mwangi',
                'category': 'research',
            },
            {
                'headline': 'AMSUN Sports Day 2026: Medics Triumph in Inter-Faculty Games',
                'content': 'The annual AMSUN Sports Day held at Nairobi University grounds was a resounding success, with the medical school securing top positions in football, basketball, and athletics categories. Over 800 students participated across 12 sports disciplines. The event was flagged off by the Dean of Medicine, Prof. Isaac Kiplagat, who emphasized the importance of physical wellness alongside academic excellence. Medical students also won the overall trophy for best sportsmanship.',
                'published_date': today - timedelta(days=14),
                'author': 'Alex Musa',
                'category': 'sports',
            },
            {
                'headline': 'Digital Health Forum: AMSUN Members Lead Discussion on AI in Medicine',
                'content': 'AMSUN hosted its inaugural Digital Health Forum, bringing together over 200 medical students, faculty, and industry stakeholders to discuss the integration of artificial intelligence in clinical practice. Key topics included AI-powered diagnostic tools, electronic health records, and telemedicine expansion in rural Kenya. The forum culminated in a hackathon where student teams developed prototype solutions for common healthcare bottlenecks, with three projects selected for incubation support.',
                'published_date': today - timedelta(days=18),
                'author': 'Beatrice Kamau',
                'category': 'innovation',
            },
        ]
        for item in news_data:
            News.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'  Created {len(news_data)} news articles'))

        # ─── EVENTS ───────────────────────────────────────────────────────────────
        self.stdout.write('Creating Events...')
        events_data = [
            {
                'title': 'Medical Innovation & Technology Seminar',
                'description': 'A cutting-edge seminar exploring the latest developments in medical technology including AI diagnostics, robotic surgery, and digital health platforms. Guest speakers include leading clinicians and tech entrepreneurs from across East Africa.',
                'date': today + timedelta(days=5),
                'time': time(12, 0),
                'location': 'LT3 - KNH Campus',
                'host': 'AMSUN Innovation Committee',
                'category': 'workshop',
            },
            {
                'title': 'Research Methodology & Publication Skills Workshop',
                'description': 'An intensive workshop designed for medical students who want to learn the fundamentals of clinical research design, data analysis using SPSS and R, and how to write and submit manuscripts to peer-reviewed journals.',
                'date': today + timedelta(days=11),
                'time': time(9, 0),
                'location': 'Boardroom 2 - Upper Kabete Campus',
                'host': 'AMSUN Academic Affairs',
                'category': 'workshop',
            },
            {
                'title': 'Free Medical Camp - Kibera Community Outreach',
                'description': 'AMSUN invites all members to participate in the quarterly free medical camp serving the Kibera community. Services include general consultations, blood pressure screening, diabetes testing, HIV counseling, and basic eye examinations.',
                'date': today + timedelta(days=25),
                'time': time(8, 0),
                'location': 'Kibera DC Grounds, Nairobi',
                'host': 'AMSUN Welfare & Community',
                'category': 'other',
            },
            {
                'title': 'AMSUN Annual Scientific Conference 2026',
                'description': 'The flagship annual event bringing together medical students, researchers, and clinical faculty for three days of scientific presentations, poster exhibitions, skill workshops, and networking sessions. Abstract submissions are open.',
                'date': today + timedelta(days=45),
                'time': time(8, 30),
                'location': 'Chandaria Business & Incubation Centre, UoN',
                'host': 'AMSUN Executive Committee',
                'category': 'conference',
            },
            {
                'title': 'AMSUN Cultural Night 2026',
                'description': 'An evening celebrating the rich cultural diversity of medical students at UoN. Featuring traditional dances, music performances, food from different communities, and fashion showcases. All AMSUN members and their guests are welcome.',
                'date': today + timedelta(days=60),
                'time': time(17, 0),
                'location': 'Kenya National Theatre, Nairobi',
                'host': 'AMSUN Cultural Affairs',
                'category': 'cultural',
            },
            # Past events
            {
                'title': 'Alumni Mentorship Dinner 2026',
                'description': 'An exclusive evening where current medical students networked with distinguished AMSUN alumni who have excelled in various medical specialties and healthcare leadership roles across Africa.',
                'date': today - timedelta(days=55),
                'time': time(18, 30),
                'location': 'Nairobi Serena Hotel, Nairobi',
                'host': 'AMSUN Alumni Relations',
                'category': 'other',
            },
            {
                'title': 'Medical Ethics in the Age of AI',
                'description': 'An interactive lecture series examining the ethical frameworks that should govern artificial intelligence in clinical decision-making, patient privacy, and resource allocation in healthcare settings.',
                'date': today - timedelta(days=72),
                'time': time(14, 0),
                'location': 'Medical School Lecture Hall, UoN',
                'host': 'AMSUN Academic Affairs',
                'category': 'workshop',
            },
            {
                'title': 'AMSUN Inter-Faculty Sports Tournament',
                'description': 'A competitive sports day event bringing together students from medicine, pharmacy, nursing, and public health for friendly competition in football, volleyball, basketball, and athletics.',
                'date': today - timedelta(days=90),
                'time': time(8, 0),
                'location': 'UoN Main Campus Sports Grounds',
                'host': 'AMSUN Sports Committee',
                'category': 'sports',
            },
        ]
        for item in events_data:
            Events.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'  Created {len(events_data)} events'))

        # ─── BLOG ─────────────────────────────────────────────────────────────────
        self.stdout.write('Creating Blog posts...')
        blog_data = [
            {
                'title': 'The Future of Telemedicine in Kenya: A Student Perspective',
                'body': 'As medical students navigating an increasingly digital healthcare landscape, we are uniquely positioned to witness and help shape the future of telemedicine in Kenya. Over the past three years, telehealth platforms have expanded rapidly, driven by the COVID-19 pandemic and subsequent investment in digital health infrastructure. Yet significant challenges remain. Rural connectivity gaps, digital literacy barriers, and regulatory frameworks that have not kept pace with innovation continue to hamper equitable access. In this article, I explore how medical students can become advocates for thoughtful telemedicine policy and how platforms like KenyaMedConnect are bridging the urban-rural healthcare divide one consultation at a time.',
                'author': 'Dr. James Kamau',
                'category': 'healthTech',
            },
            {
                'title': 'Balancing Clinical Rotations and Academic Excellence: Practical Strategies',
                'body': 'The transition from pre-clinical to clinical years is one of the most challenging periods in a medical student\'s journey. Suddenly, the structured classroom environment gives way to the unpredictable rhythms of ward rounds, emergency calls, and the emotional weight of patient care. Drawing from the experiences of over 50 final-year students I interviewed for this piece, I outline evidence-based time management strategies, note-taking systems tailored for clinical settings, and mental health practices that have helped peers successfully navigate this demanding phase.',
                'author': 'Faith Njeri',
                'category': 'education',
            },
            {
                'title': 'Breaking the Stigma: Mental Health Conversations in Medical School',
                'body': 'Medical schools have long cultivated a culture of stoicism — the idea that a good doctor must appear unshakeable, always composed, always in control. But at what cost? Research consistently shows that medical students experience depression, anxiety, and burnout at rates significantly higher than the general population and other professional students. This article explores the cultural barriers to help-seeking in medical training and profiles several AMSUN members who have become mental health advocates within their institutions.',
                'author': 'Anita Mwangi',
                'category': 'lifestyle',
            },
            {
                'title': 'Community Health Workers: The Unsung Heroes of Kenya\'s Healthcare System',
                'body': 'During our third-year community health placement in Murang\'a County, my team and I gained an entirely new appreciation for the critical role that community health workers (CHWs) play in Kenya\'s primary healthcare delivery system. With one doctor per over 16,000 people in some rural counties, CHWs represent the first and often only point of healthcare contact for millions of Kenyans. This piece documents their stories, challenges, and the policy reforms needed to adequately support and compensate these frontline workers.',
                'author': 'Kevin Ochieng',
                'category': 'research',
            },
        ]
        for item in blog_data:
            Blog.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'  Created {len(blog_data)} blog posts'))

        # ─── RESEARCH ─────────────────────────────────────────────────────────────
        self.stdout.write('Creating Research articles...')
        research_data = [
            {
                'title': 'Antibiotic Resistance Patterns in Urban Primary Healthcare Clinics in Nairobi',
                'authors': 'J. Kamau, P. Mwangi, A. Wanjiku',
                'journal': 'Tropical Medicine Journal',
                'abstract': 'A comprehensive cross-sectional study analyzing antimicrobial resistance trends across 24 primary healthcare facilities in Nairobi between 2023 and 2025. The study identified high resistance rates to commonly prescribed first-line antibiotics including amoxicillin and trimethoprim, with implications for empirical treatment protocols in urban settings.',
                'link': 'https://example.com/research/antibiotic-resistance',
            },
            {
                'title': 'Mental Health Outcomes Among Medical Students at the University of Nairobi',
                'authors': 'A. Wanjiku, M. Ali, S. Otieno',
                'journal': 'East African Medical Journal',
                'abstract': 'A longitudinal cohort study examining stress levels, burnout indicators, and coping mechanisms among 320 medical students across all six years of study at the University of Nairobi. The study found a significant increase in burnout indicators during the transition from pre-clinical to clinical years, with female students reporting higher emotional exhaustion scores.',
                'link': 'https://example.com/research/mental-health-students',
            },
            {
                'title': 'Barriers and Facilitators to Telemedicine Adoption in Rural Kenya',
                'authors': 'P. Mwangi, J. Kariuki, E. Oduya',
                'journal': 'Digital Health Innovations',
                'abstract': 'A mixed-methods study exploring the barriers and facilitators to telemedicine implementation across six rural counties in Kenya. Through 48 in-depth interviews and a survey of 210 community health workers, the study identified connectivity infrastructure, patient digital literacy, and clinician trust as the primary determinants of telemedicine uptake.',
                'link': 'https://example.com/research/telemedicine-rural-kenya',
            },
            {
                'title': 'Community-Based Nutritional Interventions for Maternal Health in Informal Settlements',
                'authors': 'S. Otieno, B. Kamau, G. Njoroge',
                'journal': 'Public Health Nutrition',
                'abstract': 'A randomized controlled trial evaluating the impact of targeted nutritional supplementation on maternal and neonatal outcomes among 480 pregnant women in three informal settlements in Nairobi. The intervention group showed statistically significant improvements in birth weight, maternal hemoglobin levels, and breastfeeding initiation rates compared to controls.',
                'link': 'https://example.com/research/maternal-nutrition',
            },
        ]
        for item in research_data:
            Research.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'  Created {len(research_data)} research articles'))

        self.stdout.write(self.style.SUCCESS('\n✅ All dummy data generated successfully!'))
        self.stdout.write(f'   News: {News.objects.count()}')
        self.stdout.write(f'   Events: {Events.objects.count()}')
        self.stdout.write(f'   Blog: {Blog.objects.count()}')
        self.stdout.write(f'   Research: {Research.objects.count()}')
