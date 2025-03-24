from django.shortcuts import render


def home(request):
    # banner = get_object_or_404(Banner, page='home')
    # projects = Project.objects.prefetch_related('technologies').order_by('created_date')
    # testimonials = Testimonial.objects.all()
    #
    # context = {
    #     'projects': projects,
    #     'banner': banner,
    #     'testimonials': testimonials,
    # }
    return render(request, 'pages/home.html')
