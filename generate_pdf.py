"""
ATS-friendly PDF generator using ReportLab.
Generates 3 clean, single-column PDFs from resume content.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, ListFlowable, ListItem
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

os.makedirs('downloads', exist_ok=True)

# Color constants
C_DARK   = colors.HexColor('#0f172a')
C_MID    = colors.HexColor('#334155')
C_LIGHT  = colors.HexColor('#475569')
C_RULE   = colors.HexColor('#94a3b8')
C_WHITE  = colors.white

# Margin: 15mm sides, 12mm top/bottom (ATS compliant, matches docx)
MARGIN_H = 15 * mm
MARGIN_V = 12 * mm

def build_styles():
    s = {}

    s['name'] = ParagraphStyle('name',
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=C_DARK, alignment=TA_CENTER, spaceAfter=3)

    s['subtitle'] = ParagraphStyle('subtitle',
        fontName='Helvetica', fontSize=10, leading=13,
        textColor=C_MID, alignment=TA_CENTER, spaceAfter=3)

    s['contact'] = ParagraphStyle('contact',
        fontName='Helvetica', fontSize=9, leading=12,
        textColor=C_LIGHT, alignment=TA_CENTER, spaceAfter=10)

    s['heading'] = ParagraphStyle('heading',
        fontName='Helvetica-Bold', fontSize=11, leading=14,
        textColor=C_DARK, spaceBefore=12, spaceAfter=4)

    s['entry_title'] = ParagraphStyle('entry_title',
        fontName='Helvetica-Bold', fontSize=10, leading=13,
        textColor=C_DARK, spaceBefore=6, spaceAfter=1)

    s['entry_meta'] = ParagraphStyle('entry_meta',
        fontName='Helvetica-Oblique', fontSize=9.5, leading=12,
        textColor=C_MID, spaceBefore=0, spaceAfter=2)

    s['body'] = ParagraphStyle('body',
        fontName='Helvetica', fontSize=9.5, leading=13,
        textColor=C_MID, spaceBefore=1, spaceAfter=1,
        alignment=TA_LEFT)

    s['bullet'] = ParagraphStyle('bullet',
        fontName='Helvetica', fontSize=9.5, leading=13,
        textColor=C_MID, spaceBefore=1, spaceAfter=1,
        leftIndent=12, bulletIndent=0)

    s['cert'] = ParagraphStyle('cert',
        fontName='Helvetica', fontSize=9.5, leading=13,
        textColor=C_MID, spaceBefore=1, spaceAfter=2,
        leftIndent=12, bulletIndent=0)

    return s

def hr(doc_width):
    return HRFlowable(width='100%', thickness=0.5, color=C_RULE, spaceAfter=4, spaceBefore=0)

def section_heading(text, styles):
    return [Paragraph(text.upper(), styles['heading']), hr(None)]

def entry_header(title, meta, styles):
    items = [Paragraph(title, styles['entry_title'])]
    if meta:
        items.append(Paragraph(meta, styles['entry_meta']))
    return items

def bullet_item(text, styles, bold_prefix=''):
    if bold_prefix:
        full = f'<b>{bold_prefix}</b>{text}'
    else:
        full = text
    return Paragraph(f'• &nbsp; {full}', styles['bullet'])

def cert_item(text, styles):
    return Paragraph(f'• &nbsp; {text}', styles['cert'])


def generate_pdf(filename, lang='id'):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=MARGIN_H,
        leftMargin=MARGIN_H,
        topMargin=MARGIN_V,
        bottomMargin=MARGIN_V,
    )

    styles = build_styles()
    story = []

    # ── HEADER ──────────────────────────────────────────────
    story.append(Paragraph('FASHA ADITYA FEBRIANTO', styles['name']))
    if lang == 'id':
        story.append(Paragraph(
            'Teknik Industri (Industrial Engineering) • Institut Teknologi Nasional (ITENAS) Bandung',
            styles['subtitle']
        ))
    else:
        story.append(Paragraph(
            'Industrial Engineering Undergraduate • National Institute of Technology (ITENAS) Bandung',
            styles['subtitle']
        ))
    story.append(Paragraph(
        'Bandung, Indonesia  •  +62 812-3456-7890  •  fshaditya@gmail.com  •  linkedin.com/in/fashaaditya  •  github.com/fshaditya',
        styles['contact']
    ))
    story.append(hr(None))

    # ── RINGKASAN / PROFESSIONAL SUMMARY ────────────────────
    story.extend(section_heading('RINGKASAN PROFESIONAL' if lang == 'id' else 'PROFESSIONAL SUMMARY', styles))
    if lang == 'id':
        story.append(Paragraph(
            'Mahasiswa Teknik Industri Institut Teknologi Nasional (ITENAS) Bandung angkatan 2025 dengan fokus keilmuan pada '
            'Perancangan Sistem Manufaktur, Pengendalian Mutu Statistika (SQC), Manajemen Persediaan, dan Analisis Data Industri. '
            'Tersertifikasi resmi Google Data Analytics dan Pemrograman Python. Berpengalaman praktis dalam pemodelan 3D CAD SolidWorks, '
            'prototipe manufaktur aditif 3D printing FDM, dan pengolahan data statistik industri berbasis Python (Pandas/NumPy). '
            'Aktif berkontribusi dalam Google Developer Groups (GDG) On Campus serta forum pemuda kewirausahaan internasional ASEAN.',
            styles['body']
        ))
    else:
        story.append(Paragraph(
            'Industrial Engineering undergraduate at Institut Teknologi Nasional (ITENAS) Bandung (Class of 2025) specializing in '
            'Manufacturing Systems Optimization, Statistical Quality Control (SQC), Inventory Management, and Industrial Data Analytics. '
            'Certified in Google Data Analytics and Python Programming. Hands-on experience in SolidWorks 3D CAD modeling, FDM 3D printing prototyping, '
            'and statistical process control using Python (Pandas/NumPy). Active member of Google Developer Groups (GDG) On Campus and regional '
            'youth enterprise summits across Southeast Asia.',
            styles['body']
        ))

    # ── PENDIDIKAN / EDUCATION ───────────────────────────────
    story.extend(section_heading('PENDIDIKAN' if lang == 'id' else 'EDUCATION', styles))
    if lang == 'id':
        story.extend(entry_header(
            'Institut Teknologi Nasional (ITENAS), Bandung',
            'Sarjana Teknik (S1) - Teknik Industri  |  September 2025 – Juni 2029 (Perkiraan Lulus)',
            styles
        ))
        story.append(bullet_item('Pengendalian Mutu Statistika (SQC), Perancangan Tata Letak Pabrik, Analisis Ergonomi & Pengukuran Kerja (RULA/REBA), Riset Operasional, Manajemen Persediaan (EOQ/ROP), K3 Industri.', styles, 'Mata Kuliah Utama: '))
        story.append(bullet_item('Anggota Aktif Google Developer Groups (GDG) On Campus ITENAS, Panitia Divisi Human Capital BIG FAIR ITENAS.', styles, 'Aktivitas Kampus: '))
    else:
        story.extend(entry_header(
            'National Institute of Technology (ITENAS), Bandung, Indonesia',
            'Bachelor of Science (B.S.) in Industrial Engineering  |  September 2025 – June 2029 (Expected)',
            styles
        ))
        story.append(bullet_item('Statistical Quality Control (SQC), Facility Layout Optimization, Ergonomics & Work Study (RULA/REBA), Operations Research, Inventory Control (EOQ/ROP), Industrial Safety.', styles, 'Core Coursework: '))
        story.append(bullet_item('Active Member at Google Developer Groups (GDG) On Campus ITENAS, Human Capital & Media Committee at BIG FAIR ITENAS.', styles, 'Campus Involvements: '))

    # ── PENGALAMAN KERJA & PROYEK / WORK EXPERIENCE & PROJECTS ─
    story.extend(section_heading('PENGALAMAN KERJA & PROYEK' if lang == 'id' else 'WORK EXPERIENCE & PROJECTS', styles))

    projects = [
        {
            'title_id': '1. Additive Manufacturing & 3D Printing Prototyping Komponen Ragum',
            'title_en': '1. Additive Manufacturing & 3D Printing Prototyping',
            'org_id':   'Laboratorium Small Scale Manufacturing (SSML) ITENAS  |  September 2025 – Oktober 2025',
            'org_en':   'Small Scale Manufacturing Laboratory (SSML) ITENAS  |  September 2025 – October 2025',
            'bullets_id': [
                ('Perancangan CAD & Optimasi Cetak: ', 'Merancang model 3D CAD komponen mekanikal ragum kerja bangku, mengonversi geometri ke format STL, dan mengoptimasi parameter cetak FDM (infill 20%, layer height 0.2 mm).'),
                ('Pemetaan Alur Proses: ', 'Menyusun diagram alir proses manufaktur aditif menggunakan Draw.io serta mengevaluasi toleransi deviasi dimensi hasil cetak filamen skala laboratorium.'),
            ],
            'bullets_en': [
                ('CAD & Slicing Optimization: ', 'Engineered 3D CAD mechanical components for an industrial bench vise, exported geometry to production STL formats, and optimized FDM printing parameters (20% infill, 0.2 mm layer height).'),
                ('Manufacturing Workflow: ', 'Formulated systematic manufacturing process flowcharts in Draw.io and inspected dimensional precision against CAD design tolerances.'),
            ],
        },
        {
            'title_id': '2. 3D Mechanical Assembly & ISO Standard Engineering Drawing Ragum SSML',
            'title_en': '2. 3D Mechanical Assembly & ISO Standard Engineering Drawing',
            'org_id':   'Laboratorium Small Scale Manufacturing (SSML) ITENAS  |  Oktober 2025 – November 2025',
            'org_en':   'Small Scale Manufacturing Laboratory (SSML) ITENAS  |  October 2025 – November 2025',
            'bullets_id': [
                ('Pemodelan Rakitan Kinematika: ', 'Membangun rakitan mekanis 3D utuh berisi 10+ komponen pada SolidWorks dengan batasan suaian (mating) dan validasi kinematika gerakan ulir penggerak.'),
                ('Dokumentasi ISO & Gambar Kerja: ', 'Menyusun dokumentasi lembar gambar kerja 2D berstandar ISO lengkap dengan proyeksi ortogonal, potongan penampang, Bill of Materials (BOM), dan toleransi geometris (GD&T).'),
            ],
            'bullets_en': [
                ('3D Kinematic Assembly: ', 'Constructed a comprehensive 10+ part mechanical assembly of a precision bench vise in SolidWorks, implementing concentric and distance mates to validate mechanical kinematic motion.'),
                ('ISO Technical Blueprints: ', 'Drafted ISO-standard 2D manufacturing drawings featuring orthogonal projections, section views, Bill of Materials (BOM), and GD&T geometric tolerance specifications.'),
            ],
        },
        {
            'title_id': '3. Statistika Deskriptif & Pengendalian Variasi Mutu Bobot Produk Manufaktur',
            'title_en': '3. Descriptive Statistics & Manufacturing QC Variance Analysis',
            'org_id':   'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS  |  November 2025 – Desember 2025',
            'org_en':   'Industrial Computing & Info Systems Lab (LKISI) ITENAS  |  November 2025 – December 2025',
            'bullets_id': [
                ('Otomasi Analisis Data Python: ', 'Mengembangkan skrip otomasi pengolahan data menggunakan Python (Pandas & NumPy) untuk menganalisis 100+ sampel variasi bobot produk manufaktur dari lini produksi.'),
                ('Evaluasi Metrik Mutu & Outlier: ', 'Mengalkulasi nilai tendensi sentral (Mean, Median, Modus), dispersi (Variansi, Standar Deviasi), serta memvisualisasikan skewness dan outlier melalui Boxplot Matplotlib.'),
            ],
            'bullets_en': [
                ('Automated Data Pipeline: ', 'Developed Python data analysis scripts (Pandas/NumPy) to assess weight variances across 100+ manufacturing production batch records.'),
                ('Dispersion & Quality Metrics: ', 'Evaluated central tendency (Mean, Median, Mode), variance, standard deviation, and quantiles; generated Boxplots and distribution metrics to identify production outliers.'),
            ],
        },
        {
            'title_id': '4. Simulasi Distribusi Sampling & Validasi Empiris Central Limit Theorem',
            'title_en': '4. Sampling Distribution Simulation & Central Limit Theorem Validation',
            'org_id':   'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS  |  Desember 2025 – Januari 2026',
            'org_en':   'Industrial Computing & Info Systems Lab (LKISI) ITENAS  |  December 2025 – January 2026',
            'bullets_id': [
                ('Simulasi Sampling Komputasional: ', 'Memodelkan simulasi komputasional distribusi sampling rata-rata berbasis Python pada berbagai skenario ukuran sampel (N=2, N=5, N=10) dari data operasional.'),
                ('Validasi Teorema Limit Pusat: ', 'Menerapkan Aturan Sturges untuk pembagian kelas frekuensi dan membuktikan secara empiris konvergensi bentuk kurva menuju distribusi normal standar.'),
            ],
            'bullets_en': [
                ('Empirical Sampling Modeling: ', 'Programmed computational sampling distribution simulations in Python across multi-sample regimes (N=2, N=5, N=10) to analyze operational population statistics.'),
                ('Central Limit Theorem Proof: ', 'Implemented Sturges Rule binning and Matplotlib histogram plotting to demonstrate mathematical convergence toward standard normal distributions.'),
            ],
        },
        {
            'title_id': '5. Pengembangan Sistem Otomasi POS & Transaksi Loyalitas Pelanggan',
            'title_en': '5. Automated Retail POS & Customer Loyalty Transaction System',
            'org_id':   'Laboratorium Komputasi Industri & Sistem Informasi (LKISI) ITENAS  |  Januari 2026 – Februari 2026',
            'org_en':   'Industrial Computing & Info Systems Lab (LKISI) ITENAS  |  January 2026 – February 2026',
            'bullets_id': [
                ('Arsitektur Alur Proses: ', 'Memodelkan sistem alur transaksi kasir retail multi-kondisi ke dalam diagram alir (flowchart) terstruktur menggunakan Microsoft Visio.'),
                ('Pengembangan Engine Transaksi: ', 'Membangun program CLI transaksi kasir berbasis Python dengan logika diskon bertingkat (cashback 8%), validasi format input, dan penerbitan ID transaksi unik.'),
            ],
            'bullets_en': [
                ('System Architecture: ', 'Architected structured retail checkout process flowcharts in Microsoft Visio mapping multi-tier transactional logic and customer membership rules.'),
                ('Python Checkout Engine: ', 'Built a Python-based order fulfillment script with conditional logic branches, automated transaction ID hashing, input validation, and real-time loyalty cashback calculation.'),
            ],
        },
    ]

    for p in projects:
        if lang == 'id':
            story.extend(entry_header(p['title_id'], p['org_id'], styles))
            for bp, bt in p['bullets_id']:
                story.append(bullet_item(bt, styles, bp))
        else:
            story.extend(entry_header(p['title_en'], p['org_en'], styles))
            for bp, bt in p['bullets_en']:
                story.append(bullet_item(bt, styles, bp))

    # ── PENGALAMAN ORGANISASI / LEADERSHIP ──────────────────
    story.extend(section_heading('PENGALAMAN ORGANISASI & KEPEMIMPINAN' if lang == 'id' else 'LEADERSHIP EXPERIENCE', styles))

    orgs = [
        {
            'title_id': 'Google Developer Groups (GDG) On Campus ITENAS',
            'meta_id':  'Anggota Aktif (Active Member)  |  Oktober 2025 – Sekarang',
            'title_en': 'Google Developer Groups (GDG) On Campus ITENAS',
            'meta_en':  'Active Member  |  October 2025 – Present',
            'bullet_id': 'Berpartisipasi aktif dalam lokakarya teknologi komputasi awan, eksplorasi ekosistem pengembang Google, dan kolaborasi proyek inovasi digital mahasiswa lintas jurusan.',
            'bullet_en': 'Actively participated in technology enablement sessions, Google Cloud developer ecosystems exploration, and student digital innovation initiatives across multidisciplinary teams.',
        },
        {
            'title_id': 'Kepanitiaan Program BIG FAIR ITENAS',
            'meta_id':  'Divisi Human Capital, Public Speaking & Content Creator  |  Agustus 2025 – Januari 2026',
            'title_en': 'BIG FAIR ITENAS Committee',
            'meta_en':  'Human Capital, Public Speaking & Content Creator  |  August 2025 – January 2026',
            'bullet_id': 'Mengoordinasikan puluhan relawan mahasiswa dan memproduksi materi komunikasi publik yang menjangkau ribuan audiens; dianugerahi sertifikat Human Capital Excellence.',
            'bullet_en': 'Coordinated volunteer operations, delivered public presentations, and developed digital outreach content reaching regional audiences; awarded Human Capital Excellence.',
        },
        {
            'title_id': 'Delegasi BIG FAIR CAYE ASEAN (Singapura & Malaysia)',
            'meta_id':  'Delegasi Pemuda Internasional  |  Februari 2026',
            'title_en': 'CAYE ASEAN Delegation (Singapore & Malaysia)',
            'meta_en':  'International Youth Delegate  |  February 2026',
            'bullet_id': 'Mewakili kontingen mahasiswa dalam forum pertukaran wawasan kewirausahaan dan industri pemuda ASEAN guna memperluas jejaring profesional internasional.',
            'bullet_en': 'Represented university delegation in youth enterprise summits across Singapore and Malaysia, broadening international industrial networking and supply chain perspectives.',
        },
    ]

    for o in orgs:
        if lang == 'id':
            story.extend(entry_header(o['title_id'], o['meta_id'], styles))
            story.append(bullet_item(o['bullet_id'], styles))
        else:
            story.extend(entry_header(o['title_en'], o['meta_en'], styles))
            story.append(bullet_item(o['bullet_en'], styles))

    # ── KEAHLIAN TEKNIS / TECHNICAL SKILLS ──────────────────
    story.extend(section_heading('KEAHLIAN TEKNIS' if lang == 'id' else 'TECHNICAL SKILLS', styles))
    if lang == 'id':
        story.append(bullet_item('Perancangan Tata Letak Pabrik (Plant Layout & ARC), Analisis Ergonomi (RULA & REBA), Pengendalian Persediaan (EOQ, ROP, Safety Stock), Toleransi Geometris (GD&T), Bill of Materials (BOM).', styles, 'Kompetensi Teknik Industri: '))
        story.append(bullet_item('Google Data Analytics, Pemrograman Python (Pandas, NumPy, Matplotlib), Pemodelan Spreadsheet/Excel, Pengendalian Mutu Statistika (SQC), Teorema Limit Pusat.', styles, 'Analisis Data & Pemrograman: '))
        story.append(bullet_item('SolidWorks CAD (3D Part Modeling & Assembly), Slicing 3D Printing (STL), Microsoft Visio, Draw.io.', styles, 'Software Desain & Manufaktur: '))
        story.append(bullet_item('Bahasa Indonesia (Penutur Asli), Bahasa Inggris (Tingkat Profesional); Public Speaking, Komunikasi Tim Multidisiplin.', styles, 'Bahasa & Komunikasi: '))
    else:
        story.append(bullet_item('Facility Layout Optimization (ARC), Ergonomic Risk Assessment (RULA/REBA), Inventory Modeling (EOQ, ROP, Safety Stock), Geometric Dimensioning & Tolerancing (GD&T), Bill of Materials (BOM).', styles, 'Industrial Engineering: '))
        story.append(bullet_item('Google Data Analytics, Python Programming (Pandas, NumPy, Matplotlib), Advanced Spreadsheet Modeling, Statistical Quality Control (SQC), Central Limit Theorem.', styles, 'Data Analytics & Programming: '))
        story.append(bullet_item('SolidWorks CAD (3D Modeling & Kinematic Assembly), FDM 3D Printing Slicing (STL), Microsoft Visio (Process Flowcharting), Draw.io.', styles, 'Engineering Software: '))
        story.append(bullet_item('Indonesian (Native), English (Professional Working Proficiency); Public Speaking, Technical Documentation, Cross-Functional Team Leadership.', styles, 'Languages & Soft Skills: '))

    # ── SERTIFIKASI / CERTIFICATIONS ────────────────────────
    story.extend(section_heading('SERTIFIKASI & PELATIHAN' if lang == 'id' else 'CERTIFICATIONS', styles))
    certs_id = [
        'Google Data Analytics Professional Certificate – Google Skillshop (Juli 2025)',
        'AI for Everyone: Master the Basics – AI Competency Certification (Agustus 2025)',
        'Memulai Pemrograman dengan Python – Dicoding Academy (September 2025)',
        'Introduction to Financial Literacy – Dicoding Academy (Oktober 2025)',
        'Human Capital Excellence & Public Speaking – BIG FAIR ITENAS (November 2025)',
        'Active Membership Credential – Google Developer Groups (GDG) On Campus (Oktober 2025)',
        'BIG FAIR CAYE ASEAN Youth Delegate 2026 – CAYE ASEAN, Singapura & Malaysia (Februari 2026)',
        'POLBAN Entrepreneur Day 2025 – Politeknik Negeri Bandung (Mei 2025)',
    ]
    certs_en = [
        'Google Data Analytics Professional Certificate – Google Skillshop (July 2025)',
        'AI for Everyone: Master the Basics – AI Competency Certification (August 2025)',
        'Programming with Python – Dicoding Academy (September 2025)',
        'Introduction to Financial Literacy – Dicoding Academy (October 2025)',
        'Human Capital Excellence & Public Speaking – BIG FAIR ITENAS (November 2025)',
        'Active Membership Credential – Google Developer Groups (GDG) On Campus (October 2025)',
        'BIG FAIR CAYE ASEAN Youth Delegate 2026 – CAYE ASEAN, Singapore & Malaysia (February 2026)',
        'POLBAN Entrepreneur Day 2025 – Politeknik Negeri Bandung (May 2025)',
    ]
    for c in (certs_id if lang == 'id' else certs_en):
        story.append(cert_item(c, styles))

    doc.build(story)
    size = os.path.getsize(filename)
    print(f'Generated: {filename} ({size:,} bytes)')


if __name__ == '__main__':
    generate_pdf('downloads/Resume_Fasha_Aditya_Febrianto_ATS.pdf', lang='id')
    generate_pdf('downloads/Resume_Fasha_Aditya_Febrianto_EN_ATS.pdf', lang='en')
    print('Done! All PDFs generated.')
