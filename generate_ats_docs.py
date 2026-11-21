import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml

os.makedirs('downloads', exist_ok=True)

def create_ats_docx(filename, lang='id', is_full_cv=False):
    doc = docx.Document()
    
    # Page setup - 0.75 inch (19.05 mm) standard ATS margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
    
    # Normal style font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(10)
    font.color.rgb = RGBColor(30, 41, 59)
    
    def add_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text.upper())
        run.bold = True
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(15, 23, 42)
        
        # Clean ATS bottom border divider
        try:
            pBrd = parse_xml(
                '<w:pBrd xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                '<w:bottom w:val="single" w:sz="6" w:space="2" w:color="94A3B8"/>'
                '</w:pBrd>'
            )
            p._p.get_or_add_pPr().append(pBrd)
        except Exception:
            pass
        return p

    def add_bullet(bold_prefix, text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.bold = True
        p.add_run(text)
        return p

    def add_entry_header(title, organization, date_range):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(5)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.keep_with_next = True
        
        r_title = p.add_run(title)
        r_title.bold = True
        
        if organization or date_range:
            p_sub = doc.add_paragraph()
            p_sub.paragraph_format.space_before = Pt(0)
            p_sub.paragraph_format.space_after = Pt(2)
            p_sub.paragraph_format.keep_with_next = True
            
            if organization:
                r_org = p_sub.add_run(organization)
                r_org.italic = True
            if organization and date_range:
                p_sub.add_run(' | ')
            if date_range:
                r_date = p_sub.add_run(date_range)
                r_date.bold = False
        return p

    # --- Header ---
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    run_name = p_name.add_run('FASHA ADITYA FEBRIANTO')
    run_name.bold = True
    run_name.font.size = Pt(18)
    run_name.font.color.rgb = RGBColor(15, 23, 42)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(3)
    run_sub = p_sub.add_run(
        'Teknik Industri (Industrial Engineering) • Institut Teknologi Nasional (ITENAS) Bandung'
        if lang == 'id'
        else 'Industrial Engineering Undergraduate • National Institute of Technology (ITENAS) Bandung'
    )
    run_sub.font.size = Pt(10)
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_after = Pt(8)
    run_contact = p_contact.add_run(
        'Bandung, Indonesia • +62 812-3456-7890 • fshaditya@gmail.com • linkedin.com/in/fashaaditya • github.com/fshaditya'
    )
    run_contact.font.size = Pt(9.5)
    run_contact.font.color.rgb = RGBColor(71, 85, 105)

    # --- Section: Professional Summary ---
    add_heading('RINGKASAN PROFESIONAL' if lang == 'id' else 'PROFESSIONAL SUMMARY')
    p_sum = doc.add_paragraph()
    p_sum.paragraph_format.space_after = Pt(4)
    p_sum.paragraph_format.line_spacing = 1.15
    if lang == 'id':
        p_sum.add_run(
            'Mahasiswa Teknik Industri Institut Teknologi Nasional (ITENAS) Bandung angkatan 2025 dengan fokus keilmuan pada '
            'Perancangan Sistem Manufaktur, Pengendalian Mutu Statistika (SQC), Manajemen Persediaan, dan Analisis Data Industri. '
            'Tersertifikasi resmi Google Data Analytics dan Pemrograman Python. Berpengalaman praktis dalam pemodelan 3D CAD SolidWorks, '
            'prototipe manufaktur aditif 3D printing FDM, dan pengolahan data statistik industri berbasis Python (Pandas/NumPy). '
            'Aktif berkontribusi dalam Google Developer Groups (GDG) On Campus serta forum pemuda kewirausahaan internasional ASEAN.'
        )
    else:
        p_sum.add_run(
            'Industrial Engineering undergraduate at Institut Teknologi Nasional (ITENAS) Bandung (Class of 2025) specializing in '
            'Manufacturing Systems Optimization, Statistical Quality Control (SQC), Inventory Management, and Industrial Data Analytics. '
            'Certified in Google Data Analytics and Python Programming. Hands-on experience in SolidWorks 3D CAD modeling, FDM 3D printing prototyping, '
            'and statistical process control using Python (Pandas/NumPy). Active member of Google Developer Groups (GDG) On Campus and regional '
            'youth enterprise summits across Southeast Asia.'
        )

    # --- Section: Education ---
    add_heading('PENDIDIKAN' if lang == 'id' else 'EDUCATION')
    add_entry_header(
        'Institut Teknologi Nasional (ITENAS), Bandung' if lang == 'id' else 'National Institute of Technology (ITENAS), Bandung, Indonesia',
        'Sarjana Teknik (S1) - Teknik Industri' if lang == 'id' else 'Bachelor of Science (B.S.) in Industrial Engineering',
        'September 2025 – Juni 2029 (Perkiraan Lulus)' if lang == 'id' else 'September 2025 – June 2029 (Expected)'
    )
    if lang == 'id':
        add_bullet('Mata Kuliah Utama: ', 'Pengendalian Mutu Statistika (SQC), Perancangan Tata Letak Pabrik, Analisis Ergonomi & Pengukuran Kerja (RULA/REBA), Riset Operasional, Manajemen Persediaan (EOQ/ROP), K3 Industri.')
        add_bullet('Aktivitas Kampus: ', 'Anggota Aktif Google Developer Groups (GDG) On Campus ITENAS, Panitia Divisi Human Capital BIG FAIR ITENAS.')
    else:
        add_bullet('Core Coursework: ', 'Statistical Quality Control (SQC), Facility Layout Optimization, Ergonomics & Work Study (RULA/REBA), Operations Research, Inventory Control (EOQ/ROP), Industrial Safety.')
        add_bullet('Campus Involvements: ', 'Active Member at Google Developer Groups (GDG) On Campus ITENAS, Human Capital & Media Committee at BIG FAIR ITENAS.')

    # --- Section: Experience & Projects (Key ATS Heading) ---
    add_heading('PENGALAMAN KERJA & PROYEK' if lang == 'id' else 'WORK EXPERIENCE & PROJECTS')

    # Project 1
    add_entry_header(
        'Additive Manufacturing & 3D Printing Prototyping Komponen Ragum' if lang == 'id' else 'Additive Manufacturing & 3D Printing Prototyping',
        'Laboratorium Small Scale Manufacturing (SSML) ITENAS' if lang == 'id' else 'Small Scale Manufacturing Lab (SSML) ITENAS',
        'September 2025 – Oktober 2025' if lang == 'id' else 'September 2025 – October 2025'
    )
    if lang == 'id':
        add_bullet('Perancangan CAD & Optimasi Cetak: ', 'Merancang model 3D CAD komponen mekanikal ragum kerja bangku, mengonversi geometri ke format STL, dan mengoptimasi parameter proses cetak FDM (infill 20%, layer height 0.2 mm).')
        add_bullet('Pemetaan Alur Proses: ', 'Menyusun diagram alir proses manufaktur aditif menggunakan Draw.io serta mengevaluasi toleransi deviasi dimensi hasil cetak filamen skala laboratorium.')
    else:
        add_bullet('CAD & Slicing Optimization: ', 'Engineered 3D CAD mechanical components for an industrial bench vise, exported geometry to production STL formats, and optimized FDM printing parameters (20% infill, 0.2 mm layer height).')
        add_bullet('Manufacturing Workflow: ', 'Formulated systematic manufacturing process flowcharts in Draw.io and inspected dimensional precision against CAD design tolerances.')

    # Project 2
    add_entry_header(
        '3D Mechanical Assembly & ISO Standard Engineering Drawing Ragum SSML' if lang == 'id' else '3D Mechanical Assembly & ISO Standard Engineering Drawing',
        'Laboratorium Small Scale Manufacturing (SSML) ITENAS' if lang == 'id' else 'Small Scale Manufacturing Lab (SSML) ITENAS',
        'Oktober 2025 – November 2025' if lang == 'id' else 'October 2025 – November 2025'
    )
    if lang == 'id':
        add_bullet('Pemodelan Rakitan Kinematika: ', 'Membangun rakitan mekanis 3D utuh berisi 10+ komponen pada SolidWorks dengan batasan suaian (mating) dan validasi kinematika gerakan ulir penggerak.')
        add_bullet('Dokumentasi ISO & Gambar Kerja: ', 'Menyusun dokumentasi lembar gambar kerja 2D berstandar ISO lengkap dengan proyeksi ortogonal, potongan penampang, Bill of Materials (BOM), dan toleransi geometris (GD&T).')
    else:
        add_bullet('3D Kinematic Assembly: ', 'Constructed a comprehensive 10+ part mechanical assembly of a precision bench vise in SolidWorks, implementing concentric and distance mates to validate mechanical kinematic motion.')
        add_bullet('ISO Technical Blueprints: ', 'Drafted ISO-standard 2D manufacturing drawings featuring orthogonal projections, section views, Bill of Materials (BOM), and GD&T geometric tolerance specifications.')

    # Project 3
    add_entry_header(
        'Statistika Deskriptif & Pengendalian Variasi Mutu Bobot Produk Manufaktur' if lang == 'id' else 'Descriptive Statistics & Manufacturing QC Variance Analysis',
        'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS' if lang == 'id' else 'Industrial Computing & Info Systems Lab (LKISI) ITENAS',
        'November 2025 – Desember 2025' if lang == 'id' else 'November 2025 – December 2025'
    )
    if lang == 'id':
        add_bullet('Otomasi Analisis Data Python: ', 'Mengembangkan skrip otomasi pengolahan data menggunakan Python (Pandas & NumPy) untuk menganalisis 100+ sampel variasi bobot produk manufaktur dari lini produksi.')
        add_bullet('Evaluasi Metrik Mutu & Outlier: ', 'Mengalkulasi nilai tendensi sentral (Mean, Median, Modus), dispersi (Variansi, Standar Deviasi), serta memvisualisasikan skewness dan outlier melalui Boxplot Matplotlib.')
    else:
        add_bullet('Automated Data Pipeline: ', 'Developed Python data analysis scripts (Pandas/NumPy) to assess weight variances across 100+ manufacturing production batch records.')
        add_bullet('Dispersion & Quality Metrics: ', 'Evaluated central tendency (Mean, Median, Mode), variance, standard deviation, and quantiles; generated Boxplots and distribution metrics to identify production outliers.')

    # Project 4
    add_entry_header(
        'Simulasi Distribusi Sampling & Validasi Empiris Central Limit Theorem' if lang == 'id' else 'Sampling Distribution Simulation & Central Limit Theorem Validation',
        'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS' if lang == 'id' else 'Industrial Computing & Info Systems Lab (LKISI) ITENAS',
        'Desember 2025 – Januari 2026' if lang == 'id' else 'December 2025 – January 2026'
    )
    if lang == 'id':
        add_bullet('Simulasi Sampling Komputasional: ', 'Memodelkan simulasi komputasional distribusi sampling rata-rata berbasis Python pada berbagai skenario ukuran sampel (N=2, N=5, N=10) dari data operasional.')
        add_bullet('Validasi Teorema Limit Pusat: ', 'Menerapkan Aturan Sturges untuk pembagian kelas frekuensi dan membuktikan secara empiris konvergensi bentuk kurva menuju distribusi normal standar.')
    else:
        add_bullet('Empirical Sampling Modeling: ', 'Programmed computational sampling distribution simulations in Python across multi-sample regimes (N=2, N=5, N=10) to analyze operational population statistics.')
        add_bullet('Central Limit Theorem Proof: ', 'Implemented Sturges Rule binning and Matplotlib histogram plotting to demonstrate mathematical convergence toward standard normal distributions.')

    # Project 5
    add_entry_header(
        'Pengembangan Sistem Otomasi POS & Transaksi Loyalitas Pelanggan' if lang == 'id' else 'Automated Retail POS & Customer Loyalty Transaction System',
        'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS' if lang == 'id' else 'Industrial Computing & Info Systems Lab (LKISI) ITENAS',
        'Januari 2026 – Februari 2026' if lang == 'id' else 'January 2026 – February 2026'
    )
    if lang == 'id':
        add_bullet('Arsitektur Alur Proses: ', 'Memodelkan sistem alur transaksi kasir retail multi-kondisi ke dalam diagram alir (flowchart) terstruktur menggunakan Microsoft Visio.')
        add_bullet('Pengembangan Engine Transaksi: ', 'Membangun program CLI transaksi kasir berbasis Python dengan logika diskon bertingkat (cashback 8%), validasi format input, dan penerbitan ID transaksi unik.')
    else:
        add_bullet('System Architecture: ', 'Architected structured retail checkout process flowcharts in Microsoft Visio mapping multi-tier transactional logic and customer membership rules.')
        add_bullet('Python Checkout Engine: ', 'Built a Python-based order fulfillment script with conditional logic branches, automated transaction ID hashing, input validation, and real-time loyalty cashback calculation.')

    # --- Section: Leadership & Organizational Experience ---
    add_heading('PENGALAMAN ORGANISASI & KEPEMIMPINAN' if lang == 'id' else 'LEADERSHIP EXPERIENCE')
    if lang == 'id':
        add_entry_header(
            'Google Developer Groups (GDG) On Campus ITENAS',
            'Anggota Aktif (Active Member)',
            'Oktober 2025 – Sekarang'
        )
        add_bullet('', 'Berpartisipasi aktif dalam lokakarya teknologi komputasi awan, eksplorasi ekosistem pengembang Google, dan kolaborasi proyek inovasi digital mahasiswa lintas jurusan.')

        add_entry_header(
            'Kepanitiaan Program BIG FAIR ITENAS',
            'Divisi Human Capital, Public Speaking & Content Creator',
            'Agustus 2025 – Januari 2026'
        )
        add_bullet('', 'Mengoordinasikan puluhan relawan mahasiswa dan memproduksi materi komunikasi publik yang menjangkau ribuan audiens; dianugerahi sertifikat Human Capital Excellence.')

        add_entry_header(
            'Delegasi BIG FAIR CAYE ASEAN (Singapura & Malaysia)',
            'Delegasi Pemuda Internasional',
            'Februari 2026 – Februari 2026'
        )
        add_bullet('', 'Mewakili kontingen mahasiswa dalam forum pertukaran wawasan kewirausahaan dan industri pemuda ASEAN guna memperluas jejaring profesional internasional.')
    else:
        add_entry_header(
            'Google Developer Groups (GDG) On Campus ITENAS',
            'Active Member',
            'October 2025 – Present'
        )
        add_bullet('', 'Actively participated in technology enablement sessions, Google Cloud developer ecosystems exploration, and student digital innovation initiatives across multidisciplinary teams.')

        add_entry_header(
            'BIG FAIR ITENAS Committee',
            'Human Capital, Public Speaking & Content Creator',
            'August 2025 – January 2026'
        )
        add_bullet('', 'Coordinated volunteer operations, delivered public presentations, and developed digital outreach content reaching regional audiences; awarded Human Capital Excellence.')

        add_entry_header(
            'CAYE ASEAN Delegation (Singapore & Malaysia)',
            'International Youth Delegate',
            'February 2026 – February 2026'
        )
        add_bullet('', 'Represented university delegation in youth enterprise summits across Singapore and Malaysia, broadening international industrial networking and supply chain perspectives.')

    # --- Section: Skills ---
    add_heading('KEAHLIAN TEKNIS' if lang == 'id' else 'TECHNICAL SKILLS')
    if lang == 'id':
        add_bullet('Kompetensi Teknik Industri: ', 'Perancangan Tata Letak Pabrik (Plant Layout & ARC), Analisis Ergonomi (RULA & REBA), Pengendalian Persediaan (EOQ, ROP, Safety Stock), Toleransi Geometris (GD&T), Bill of Materials (BOM).')
        add_bullet('Analisis Data & Pemrograman: ', 'Google Data Analytics, Pemrograman Python (Pandas, NumPy, Matplotlib), Pemodelan Spreadsheet / Excel, Pengendalian Mutu Statistika (SQC), Teorema Limit Pusat.')
        add_bullet('Software Desain & Manufaktur: ', 'SolidWorks CAD (3D Part Modeling & Assembly), Slicing 3D Printing (STL), Microsoft Visio (Pemodelan Flowchart), Draw.io.')
        add_bullet('Bahasa & Komunikasi: ', 'Bahasa Indonesia (Penutur Asli), Bahasa Inggris (Tingkat Profesional); Public Speaking, Komunikasi Tim Multidisiplin.')
    else:
        add_bullet('Industrial Engineering: ', 'Facility Layout Optimization (ARC), Ergonomic Risk Assessment (RULA/REBA), Inventory Modeling (EOQ, ROP, Safety Stock), Geometric Dimensioning & Tolerancing (GD&T), Bill of Materials (BOM).')
        add_bullet('Data Analytics & Programming: ', 'Google Data Analytics, Python Programming (Pandas, NumPy, Matplotlib), Advanced Spreadsheet Modeling, Statistical Quality Control (SQC), Central Limit Theorem.')
        add_bullet('Engineering Software: ', 'SolidWorks CAD (3D Modeling & Kinematic Assembly), FDM 3D Printing Slicing (STL), Microsoft Visio (Process Flowcharting), Draw.io.')
        add_bullet('Languages & Soft Skills: ', 'Indonesian (Native), English (Professional Working Proficiency); Public Speaking, Technical Documentation, Cross-Functional Team Leadership.')

    # --- Section: Certifications ---
    add_heading('SERTIFIKASI & PELATIHAN' if lang == 'id' else 'CERTIFICATIONS')
    certs_id = [
        ('Google Data Analytics Professional Certificate', 'Google Skillshop', 'Juli 2025'),
        ('AI for Everyone: Master the Basics', 'AI Competency Certification', 'Agustus 2025'),
        ('Memulai Pemrograman dengan Python', 'Dicoding Academy', 'September 2025'),
        ('Introduction to Financial Literacy', 'Dicoding Academy', 'Oktober 2025'),
        ('Human Capital Excellence & Public Speaking', 'BIG FAIR ITENAS', 'November 2025'),
        ('Active Membership Credential', 'Google Developer Groups (GDG) On Campus', 'Oktober 2025'),
        ('BIG FAIR CAYE ASEAN Youth Delegate 2026', 'CAYE ASEAN (Singapura & Malaysia)', 'Februari 2026'),
        ('POLBAN Entrepreneur Day 2025', 'Politeknik Negeri Bandung', 'Mei 2025')
    ]
    certs_en = [
        ('Google Data Analytics Professional Certificate', 'Google Skillshop', 'July 2025'),
        ('AI for Everyone: Master the Basics', 'AI Competency Certification', 'August 2025'),
        ('Programming with Python', 'Dicoding Academy', 'September 2025'),
        ('Introduction to Financial Literacy', 'Dicoding Academy', 'October 2025'),
        ('Human Capital Excellence & Public Speaking', 'BIG FAIR ITENAS', 'November 2025'),
        ('Active Membership Credential', 'Google Developer Groups (GDG) On Campus', 'October 2025'),
        ('BIG FAIR CAYE ASEAN Youth Delegate 2026', 'CAYE ASEAN (Singapore & Malaysia)', 'February 2026'),
        ('POLBAN Entrepreneur Day 2025', 'Politeknik Negeri Bandung', 'May 2025')
    ]
    certs = certs_id if lang == 'id' else certs_en
    for c_title, c_issuer, c_date in certs:
        add_bullet(f'{c_title} – {c_issuer}', f' ({c_date})')

    doc.save(filename)
    print(f'Generated: {filename} ({os.path.getsize(filename)} bytes)')

if __name__ == '__main__':
    create_ats_docx('downloads/Resume_Fasha_Aditya_Febrianto_ATS.docx', lang='id')
    create_ats_docx('downloads/Resume_Fasha_Aditya_Febrianto_EN_ATS.docx', lang='en')
    create_ats_docx('downloads/CV_Fasha_Aditya_Febrianto_ATS.docx', lang='id', is_full_cv=True)
