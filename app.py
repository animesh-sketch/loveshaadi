import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ShaadiZone - Premium Matrimony", page_icon="👑", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Poppins:wght@300;400;500;600&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
    }
    
    .hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 80px 40px;
        border-radius: 0;
        text-align: center;
        color: white;
        margin-bottom: 60px;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="0.5"/></svg>');
        background-size: 200px;
    }
    .hero h1 { 
        font-size: 4rem; 
        margin-bottom: 20px; 
        font-weight: 700;
        letter-spacing: 2px;
    }
    .hero p { 
        font-size: 1.5rem; 
        opacity: 0.9; 
        font-weight: 300;
    }
    .stats { 
        display: flex; 
        justify-content: center; 
        gap: 80px; 
        margin-top: 40px; 
    }
    .stat-item { 
        text-align: center; 
    }
    .stat-number { 
        font-size: 2.5rem; 
        font-weight: 700;
        font-family: 'Playfair Display', serif;
    }
    .stat-label {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        opacity: 0.8;
    }
    .feature-card {
        background: white;
        padding: 40px 30px;
        border-radius: 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.12);
    }
    .success-story {
        background: white;
        padding: 35px;
        border-radius: 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        border-left: 4px solid #c9a962;
    }
    .mission-box {
        background: linear-gradient(135deg, #fdfbf7, #f5f0e8);
        padding: 50px;
        border-radius: 0;
        border: 1px solid #c9a962;
        margin: 40px 0;
        text-align: center;
    }
    .gold-text {
        color: #c9a962;
    }
    .profile-card {
        background: white;
        border-radius: 0;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.12);
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #c9a962, transparent);
        margin: 40px 0;
    }
    .elegant-btn {
        background: linear-gradient(135deg, #c9a962, #b8954f);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    .elegant-btn:hover {
        background: linear-gradient(135deg, #b8954f, #c9a962);
        transform: translateY(-2px);
    }
    .nav-container {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid #f0f0f0;
        padding: 20px 0;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .footer {
        background: #1a1a2e;
        color: white;
        padding: 60px 0 30px;
        margin-top: 80px;
    }
    .footer-title {
        color: #c9a962;
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        margin-bottom: 20px;
    }
    .profile-header {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 60px;
        border-radius: 0;
    }
    .detail-card {
        background: white;
        padding: 30px;
        border-radius: 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
    }
    .preference-item {
        background: linear-gradient(135deg, #fdfbf7, #f5f0e8);
        padding: 25px;
        border-radius: 0;
        text-align: center;
        border: 1px solid #c9a962;
    }
    .verified-badge {
        background: linear-gradient(135deg, #c9a962, #b8954f);
        color: white;
        padding: 8px 20px;
        font-size: 0.85rem;
        letter-spacing: 1px;
    }
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 50px;
        position: relative;
    }
    .section-title::after {
        content: '';
        display: block;
        width: 60px;
        height: 3px;
        background: #c9a962;
        margin: 20px auto 0;
    }
    .form-container {
        background: white;
        padding: 50px;
        border-radius: 0;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
        border: 1px solid #f0f0f0;
    }
    .stButton > button {
        border-radius: 0;
    }
    input, select, textarea {
        border-radius: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

if 'profiles' not in st.session_state:
    st.session_state.profiles = [
        {"id": 1, "name": "Princess Priya Sharma", "age": 26, "profession": "Software Engineer", "location": "Mumbai", "education": "B.Tech", "religion": "Hindu", "image": "👸", "verified": True, "about": "Elegant soul with a kind heart. I believe in traditional values with a modern outlook. Looking for someone who appreciates the finer things in life.", "disability": "Wheelchair User", "disability_type": "Physical", "income": "8-10 LPA"},
        {"id": 2, "name": "Royal Rahul Verma", "age": 28, "profession": "Doctor", "location": "Delhi", "education": "MBBS", "religion": "Hindu", "image": "🤴", "verified": True, "about": "A gentleman who believes in service before self. Seeking a partner who values honesty, loyalty, and family traditions.", "disability": "Physically Challenged", "disability_type": "Physical", "income": "15-20 LPA"},
        {"id": 3, "name": "Divine Anjali Patel", "age": 24, "profession": "Teacher", "location": "Ahmedabad", "education": "M.A. B.Ed", "religion": "Hindu", "image": "👩‍🏫", "verified": True, "about": "Educator with a passion for shaping young minds. My warmth extends beyond the classroom.", "disability": "Visually Impaired", "disability_type": "Visual", "income": "5-6 LPA"},
        {"id": 4, "name": "Emperor Vikram Singh", "age": 30, "profession": "Business Owner", "location": "Jaipur", "education": "MBA", "religion": "Hindu", "image": "👑", "verified": True, "about": "Building an empire with ethical values. Looking for my queen who stands by me through every challenge.", "disability": "Physical Disability", "disability_type": "Physical", "income": "25-30 LPA"},
        {"id": 5, "name": "Grace Meera Nair", "age": 27, "profession": "Fashion Designer", "location": "Bangalore", "education": "B.Des", "religion": "Hindu", "image": "👒", "verified": True, "about": "Creating beauty in every stitch. Seeking someone who sees beauty beyond appearances.", "disability": "Hearing Impaired", "disability_type": "Hearing", "income": "6-8 LPA"},
        {"id": 6, "name": "Noble Arjun Menon", "age": 29, "profession": "Senior Engineer", "location": "Kochi", "education": "B.Tech", "religion": "Hindu", "image": "🎩", "verified": True, "about": "Engineer by profession, artist by heart. Looking for a partner who appreciates sophistication.", "disability": "Physical Disability", "disability_type": "Physical", "income": "12-15 LPA"},
    ]

if 'page' not in st.session_state:
    st.session_state.page = "home"

if 'selected_profile' not in st.session_state:
    st.session_state.selected_profile = None

profile_images = ["👸", "🤴", "👑", "👒", "🎩", "💎", "🌟", "⭐", "👁️", "🦋", "🌸", "💜", "🦄", "🌙", "☀️", "💫"]
locations = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Jaipur', 'Ahmedabad', 'Kochi', 'Kolkata', 'Lucknow', 'Chandigarh', 'Surat', 'Vizag']
religions = ['Hindu', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain', 'Parsi', 'Other']
professions = ['Software Engineer', 'Doctor', 'Business Owner', 'Fashion Designer', 'Engineer', 'Architect', 'Lawyer', 'Chartered Accountant', 'Banker', 'Artist', 'Writer', 'Consultant', 'Government Employee', 'Other']
disability_types = ['Physical Disability', 'Visually Impaired', 'Hearing Impaired', 'Speech Impairment', 'Other']
income_ranges = ['Below 5 LPA', '5-10 LPA', '10-15 LPA', '15-20 LPA', '20-30 LPA', '30+ LPA', 'Prefer not to say']

def nav_to(page):
    st.session_state.page = page
    st.rerun()

def show_home():
    st.markdown("""
    <div class="hero">
        <h1>👑 ShaadiZone</h1>
        <p>Where Elegance Meets Eternal Love</p>
        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">10,000+</div>
                <div class="stat-label">Noble Members</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Success Stories</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">200+</div>
                <div class="stat-label">Happy Couples</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="mission-box">
        <h2 style="font-family: 'Playfair Display', serif; color: #1a1a2e; margin-top: 0;">✨ Our Philosophy</h2>
        <p style="font-size: 1.2rem; color: #666; max-width: 800px; margin: 20px auto; line-height: 1.8;">At ShaadiZone, we believe that true love knows no boundaries. We are dedicated to creating meaningful connections between dignified individuals who seek companionship built on trust, respect, and shared values.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### ✨ Begin Your Journey")
        st.markdown("""
        <ul style="font-size: 1.1rem; color: #666; line-height: 2;">
            <li>✨ Create an elegant profile in minutes</li>
            <li>✅ Get verified for authenticity</li>
            <li>💕 Connect with compatible partners</li>
            <li>🔒 Your privacy is our priority</li>
            <li>💎 Premium matchmaking experience</li>
        </ul>
        """, unsafe_allow_html=True)
        if st.button("Create Your Profile", type="primary", use_container_width=True):
            nav_to("create")
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fdfbf7, #f5f0e8); padding: 30px; border-left: 4px solid #c9a962;">
            <p style="font-style: italic; color: #666; font-size: 1.1rem; line-height: 1.8;">"ShaadiZone helped me find my soulmate. The platform's elegance and sophistication made my search truly special."</p>
            <p style="font-weight: 600; color: #c9a962; margin-top: 15px;">— Princess Priya & Royal Rahul</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">Why Choose ShaadiZone</h2>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    features = [
        ("💎", "Premium Experience", "Exquisite matchmaking"),
        ("🛡️", "Verified Profiles", "Authenticity guaranteed"),
        ("🤝", "Personal Matchmaker", "Dedicated support"),
        ("🔐", "Privacy Protected", "Your secrets are safe"),
    ]
    for i, (icon, title, desc) in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-size: 3rem; margin-bottom: 20px;">{icon}</div>
                <h4 style="color: #1a1a2e; margin-bottom: 10px;">{title}</h4>
                <p style="color: #888;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-title">Love Stories</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    stories = [
        ("We found each other on ShaadiZone. Our love story is proof that destiny exists!", "Princess Priya & Royal Rahul"),
        ("The platform's elegance matched our expectations. We're blessed with happiness.", "Emperor Vikram & Grace Meera"),
        ("Thank you for bringing two souls together in the most beautiful way.", "Noble Arjun & Divine Anjali"),
    ]
    for i, (quote, names) in enumerate(stories):
        with cols[i]:
            st.markdown(f"""
            <div class="success-story">
                <p style="font-style: italic; color: #666; font-size: 1.05rem; line-height: 1.8;">"{quote}"</p>
                <p style="font-weight: 600; color: #c9a962; margin-top: 20px;">— {names}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #888; font-size: 0.9rem; letter-spacing: 2px;'>Made with 💜 by Animesh | Founded by Animesh</p>", unsafe_allow_html=True)

def show_profiles():
    st.markdown('<h1 class="section-title">Our Distinguished Members</h1>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        search = st.text_input("Search", placeholder="Name...")
    with col2:
        age_filter = st.selectbox("Age", ["All Ages", "21-25", "26-30", "31-35", "35+"])
    with col3:
        loc_filter = st.selectbox("Location", ["All Cities"] + locations)
    with col4:
        dis_filter = st.selectbox("Category", ["All Categories"] + disability_types)
    with col5:
        sort_by = st.selectbox("Sort By", ["Latest", "Age: Young", "Age: Elder"])
    
    profiles = st.session_state.profiles
    
    if search:
        profiles = [p for p in profiles if search.lower() in p['name'].lower() or search.lower() in p['location'].lower()]
    if age_filter != "All Ages":
        if age_filter == "21-25":
            profiles = [p for p in profiles if p['age'] <= 25]
        elif age_filter == "26-30":
            profiles = [p for p in profiles if 25 < p['age'] <= 30]
        elif age_filter == "31-35":
            profiles = [p for p in profiles if 30 < p['age'] <= 35]
        else:
            profiles = [p for p in profiles if p['age'] > 35]
    if loc_filter != "All Cities":
        profiles = [p for p in profiles if p['location'] == loc_filter]
    if dis_filter != "All Categories":
        profiles = [p for p in profiles if dis_filter in p.get('disability', '')]
    
    st.markdown(f"<p style='text-align: center; color: #888; margin-bottom: 40px;'>{len(profiles)} distinguished members found</p>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, profile in enumerate(profiles):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"""
                <div class="profile-card">
                    <div style="background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 50px; text-align: center;">
                        <div style="font-size: 5rem;">{profile['image']}</div>
                    </div>
                    <div style="padding: 25px;">
                        <h3 style="color: #1a1a2e; margin: 0 0 10px 0; font-family: 'Playfair Display', serif;">{profile['name']}</h3>
                        <p style="color: #c9a962; font-weight: 600; margin: 0;">{profile['age']} years • {profile['location']}</p>
                        <p style="color: #666; font-size: 0.95rem; margin: 10px 0;">{profile['profession']}</p>
                        <p style="color: #888; font-size: 0.85rem;">🎓 {profile['education']}</p>
                        <p style="color: #666; font-size: 0.85rem; font-weight: 500;">♿ {profile.get('disability', 'N/A')}</p>
                        {f'<span class="verified-badge" style="display: inline-block; margin-top: 10px;">✓ VERIFIED</span>' if profile['verified'] else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"View Profile", key=f"view_{profile['id']}", use_container_width=True):
                    st.session_state.selected_profile = profile
                    st.session_state.page = "detail"
                    st.rerun()

def show_profile_detail():
    profile = st.session_state.selected_profile
    
    col1 = st.columns(1)[0]
    with col1:
        if st.button("← Back to Members"):
            st.session_state.page = "profiles"
            st.rerun()
    
    st.markdown(f"""
    <div class="profile-header">
        <div style="display: flex; align-items: center; gap: 40px;">
            <div style="background: white; padding: 30px; border-radius: 0; font-size: 6rem;">{profile['image']}</div>
            <div>
                <h1 style="color: white; margin: 0; font-family: 'Playfair Display', serif; font-size: 2.5rem;">{profile['name']}</h1>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; margin: 10px 0;">{profile['age']} years • {profile['location']}</p>
                <p style="color: rgba(255,255,255,0.9);">{profile['profession']} • {profile['education']}</p>
                <p style="background: #c9a962; color: white; padding: 8px 20px; display: inline-block; margin-top: 10px; font-size: 0.9rem;">♿ {profile.get('disability', 'N/A')}</p>
                {f'<span class="verified-badge" style="display: inline-block; margin-left: 10px;">✓ VERIFIED PROFILE</span>' if profile['verified'] else ''}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="detail-card"><h3>Personal Details</h3>', unsafe_allow_html=True)
        details = [
            ("Profession", profile['profession']),
            ("Location", profile['location']),
            ("Education", profile['education']),
            ("Religion", profile['religion']),
            ("Disability Type", profile.get('disability', 'N/A')),
            ("Annual Income", profile.get('income', 'Prefer not to say')),
        ]
        for label, value in details:
            st.markdown(f"**{label}:** {value}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="detail-card"><h3>About Me</h3>', unsafe_allow_html=True)
        st.write(profile.get('about', "A distinguished individual seeking a meaningful connection."))
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-title" style="font-size: 1.8rem;">Partner Preferences</h3>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    prefs = [("Age", "21-30 years"), ("Religion", "Any"), ("Profession", "Professional"), ("Location", "Flexible")]
    for i, (label, value) in enumerate(prefs):
        with cols[i]:
            st.markdown(f"""
            <div class="preference-item">
                <p style="color: #888; margin: 0; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">{label}</p>
                <p style="color: #1a1a2e; font-weight: 600; margin: 10px 0 0 0; font-size: 1.1rem;">{value}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("### 💕 Looking For")
    st.info("Seeking a dignified partner who values honesty, loyalty, and family traditions. Someone who understands that true beauty lies within.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💌 Express Interest", type="primary", use_container_width=True):
            st.success("Your interest has been expressed!")
    with col2:
        if st.button("⭐ Add to Shortlist", use_container_width=True):
            st.success("Added to your shortlist!")
    with col3:
        if st.button("📞 Request Contact", use_container_width=True):
            st.info("Contact request sent!")

def show_create_profile():
    st.markdown('<h1 class="section-title">Create Your Profile</h1>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #666; margin-bottom: 40px;'>Join our distinguished community of elegant souls</p>", unsafe_allow_html=True)
    
    with st.form("create_profile"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name *", placeholder="Your full name")
            age = st.number_input("Age *", min_value=21, max_value=55)
            profession = st.selectbox("Profession *", ["Select"] + professions)
            location = st.selectbox("Location *", ["Select"] + locations)
        with col2:
            education = st.text_input("Education *", placeholder="Your degree")
            religion = st.selectbox("Religion *", religions)
            income = st.selectbox("Annual Income", ["Prefer not to say"] + income_ranges)
            image = st.selectbox("Choose Your Avatar", profile_images)
        
        st.markdown("### ♿ Disability Information")
        col1, col2 = st.columns(2)
        with col1:
            disability_type = st.selectbox("Category *", ["Select"] + disability_types)
        with col2:
            disability_detail = st.text_input("Specific Details", placeholder="Brief description")
        
        about = st.text_area("About Yourself *", placeholder="Tell us about yourself, your interests, and what you seek in a partner...", height=150)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fdfbf7, #f5f0e8); padding: 20px; margin: 20px 0; border-left: 4px solid #c9a962;">
            <p style="margin: 0; color: #666;">💎 Your profile will be reviewed by our team. Verified members receive a prestigious badge!</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("Create Profile", type="primary", use_container_width=True)
        with col2:
            cancel = st.form_submit_button("Cancel", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit:
            if name and age and profession != "Select" and location != "Select" and education and about:
                new_profile = {
                    "id": len(st.session_state.profiles) + 1,
                    "name": name,
                    "age": age,
                    "profession": profession,
                    "location": location,
                    "education": education,
                    "religion": religion,
                    "image": image,
                    "verified": False,
                    "about": about,
                    "disability": disability_detail if disability_detail else disability_type,
                    "disability_type": disability_type,
                    "income": income
                }
                st.session_state.profiles.insert(0, new_profile)
                st.success("Profile created successfully! Our team will verify it soon.")
                nav_to("profiles")
            else:
                st.error("Please fill in all required fields!")
        
        if cancel:
            nav_to("home")

# Main app
nav_cols = st.columns([1, 2, 1])
with nav_cols[1]:
    nav_options = ["🏠 Home", "👥 Members", "📝 Join Now"]
    selected_nav = st.radio("Navigation", nav_options, 
                          index=0 if st.session_state.page == "home" else 1 if st.session_state.page == "profiles" else 2,
                          label_visibility="collapsed", horizontal=True)
    
    if "Home" in selected_nav and st.session_state.page != "home":
        nav_to("home")
    elif "Members" in selected_nav and st.session_state.page != "profiles":
        nav_to("profiles")
    elif "Join" in selected_nav and st.session_state.page != "create":
        nav_to("create")

if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "profiles":
    show_profiles()
elif st.session_state.page == "detail":
    show_profile_detail()
elif st.session_state.page == "create":
    show_create_profile()

st.markdown("---")
st.markdown(f"""
<div style="background: #1a1a2e; padding: 40px 0; margin-top: 60px; text-align: center;">
    <p style="color: #c9a962; font-family: 'Playfair Display', serif; font-size: 1.5rem; margin: 0;">👑 ShaadiZone</p>
    <p style="color: #888; margin-top: 10px;">Where Elegance Meets Eternal Love</p>
    <p style="color: #666; font-size: 0.85rem; margin-top: 30px;">© 2026 ShaadiZone - Premium Matrimony Services | Founded by Animesh</p>
</div>
""", unsafe_allow_html=True)
