document.addEventListener('DOMContentLoaded', () => {
    const downloadBtn = document.getElementById('downloadBtn');
    
    // Add click event listener to the download button
    downloadBtn.addEventListener('click', (e) => {
        // We can add some logic here, e.g., tracking the download
        console.log('Download initiated!');
        
        // Add a temporary loading state
        const originalText = downloadBtn.innerHTML;
        downloadBtn.innerHTML = `
            Downloading...
            <svg class="spinner" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 12a9 9 0 1 1-6.219-8.56"></path>
            </svg>
        `;
        downloadBtn.style.opacity = '0.8';
        downloadBtn.style.pointerEvents = 'none';

        // Add a bit of CSS for the spinner dynamically
        const style = document.createElement('style');
        style.innerHTML = `
            .spinner { animation: spin 1s linear infinite; margin-left: 8px; }
            @keyframes spin { 100% { transform: rotate(360deg); } }
        `;
        document.head.appendChild(style);

        // Reset button after a short delay (simulating processing)
        setTimeout(() => {
            downloadBtn.innerHTML = originalText;
            downloadBtn.style.opacity = '1';
            downloadBtn.style.pointerEvents = 'auto';
        }, 2000);
    });

    // Add parallax effect to the book cover on mouse move
    const heroVisual = document.querySelector('.hero-visual');
    const bookContainer = document.querySelector('.book-container');

    if (heroVisual && bookContainer && window.innerWidth > 992) {
        heroVisual.addEventListener('mousemove', (e) => {
            const rect = heroVisual.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * 10;
            const rotateY = ((x - centerX) / centerX) * -15 - 15; // Base rotation is -15
            
            bookContainer.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            bookContainer.style.transition = 'none';
        });

        heroVisual.addEventListener('mouseleave', () => {
            bookContainer.style.transform = `rotateY(-15deg) rotateX(5deg)`;
            bookContainer.style.transition = 'transform 0.5s ease';
        });
    }
});
