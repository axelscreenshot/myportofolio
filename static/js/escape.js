// Mengubah karakter khusus HTML menjadi entity agar ditampilkan sebagai teks
function escapeHtml(value) {
    return String(value ?? '')
        .replaceAll('&', '&amp;') // Diganti paling awal agar `&` lain tidak ikut diubah lagi
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
}
