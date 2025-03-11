from django.shortcuts import render

# Create your views here.


def services(request):
    context = {
        "services": ["Web design and development", "Digital marketing and SEO", "Graphic design", "Content writing and editing", "Business consulting", "Financial planning", "IT support and management", "Social media management", "Video production and editing", "Virtual assistant services"]
    }
    return render(request, "freelancer/services.html", context)

def testimonials(request):
    context = {
        "testimonials": {
    "Sarah Johnson": "The service exceeded my expectations! The team was professional and delivered everything on time.",
    "Michael Chen": "I was skeptical at first, but now I can't imagine running my business without their help.",
    "Priya Patel": "Their attention to detail is incredible. They caught issues I never would have noticed.",
    "James Rodriguez": "Five stars! The customer support team was responsive and solved my problem within hours.",
    "Emma Williams": "The results speak for themselves - my website traffic increased by 200% in just two months.",
    "David Kim": "Working with this team has been the best business decision I've made in years.",
    "Olivia Martinez": "They took the time to understand my unique needs and delivered a customized solution.",
    "Robert Taylor": "Transparent pricing and no hidden fees. Refreshing to work with such an honest company.",
    "Aisha Washington": "The onboarding process was seamless, and I was up and running in no time.",
    "Thomas Garcia": "Their innovative approach helped me stand out from my competitors."
}
    }
    return render(request, "freelancer/testimonials.html", context)

def pricing(request):
    context = {
        "pricing": {
    "Web design and development": "$2,500",
    "Digital marketing and SEO": "$1,800/month",
    "Graphic design": "$85/hour",
    "Content writing and editing": "$0.15/word",
    "Business consulting": "$150/hour",
    "Financial planning": "$250/session",
    "IT support and management": "$95/hour",
    "Social media management": "$950/month",
    "Video production and editing": "$1,200/project",
    "Virtual assistant services": "$35/hour"
}
    }
    return render(request, "freelancer/pricing.html", context)

def blogs(request):
    context = {
        "blogs": ["The Rise of Sustainable Living",
"In recent years, sustainable living has moved from a fringe lifestyle choice to a mainstream movement. More people are recognizing the impact their daily choices have on the environment.",
"One of the biggest trends is the shift toward minimalism. Consumers are questioning the need for excess possessions and focusing instead on quality over quantity. This has led to the popularity of capsule wardrobes, tiny homes, and zero-waste lifestyles.",
"Food choices are another area seeing significant change. Plant-based diets continue to grow in popularity, with even meat-eaters participating in movements like 'Meatless Monday.' Community gardens and farmers' markets are thriving as people seek locally-sourced produce.",
"Technology is playing a surprising role in sustainability too. Apps that help reduce food waste, platforms for sharing or renting items instead of buying, and smart home systems that optimize energy use are making sustainable choices more accessible.",
"The financial sector is also adapting, with eco-conscious investment options becoming more widely available. Many people are now considering the environmental impact of their retirement funds and investment portfolios.",
"While the challenge of climate change remains daunting, these shifts in individual behavior collectively represent a significant positive trend. The movement toward sustainable living offers hope that meaningful change is possible through individual choices multiplied across communities."]
    }
    return render(request, "freelancer/blog.html", context)

def case_studies(request):
    context = {
        "case_studies": ["Case Study 1: Tech Startup Increases Conversion Rate by 43% - A struggling SaaS company implemented targeted UX improvements based on heat map analysis, resulting in significantly improved user engagement and subscription rates within 60 days.", "Case Study 2: Manufacturing Plant Reduces Energy Costs by 31% - By installing smart monitoring systems and implementing an employee awareness program, a mid-sized manufacturer achieved substantial cost savings while reducing their carbon footprint.", "Case Study 3: Healthcare Provider Decreases Wait Times by 68% - Through process reengineering and implementing a new digital intake system, a regional clinic dramatically improved patient satisfaction while increasing daily appointment capacity.", "Case Study 4: Retail Chain Boosts Employee Retention by 27% - After implementing a comprehensive training program and adjusting compensation structures, a national retailer significantly reduced turnover rates and associated hiring costs.", "Case Study 5: Financial Services Firm Expands Market Share by 18% - Through targeted digital marketing campaigns and personalized client outreach initiatives, a boutique advisory firm successfully penetrated a new demographic segment within 12 months."]
    }

    return render(request, "freelancer/case_studies.html", context)

