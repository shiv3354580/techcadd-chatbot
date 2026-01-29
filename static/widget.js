// TechCADD Chat Widget Embed Script
(function() {
    // Create widget container
    const widgetHTML = `
        <div id="techcadd-chat-widget" style="position: fixed; bottom: 20px; right: 20px; z-index: 10000;">
            <button id="techcadd-chat-button" style="width: 60px; height: 60px; background: linear-gradient(135deg, #1a237e 0%, #283593 100%); border-radius: 50%; border: none; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center;">
                <i class="fas fa-comment-dots" style="color: white; font-size: 24px;"></i>
            </button>
            <div id="techcadd-chat-window" style="display: none; position: absolute; bottom: 70px; right: 0; width: 350px; height: 500px; background: white; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); flex-direction: column; overflow: hidden; border: 1px solid #e0e0e0;">
                <!-- Chat content will be loaded via iframe -->
                <iframe src="http://52.21.137.204/widget" style="width: 100%; height: 100%; border: none;"></iframe>
            </div>
        </div>
    `;
    
    // Add Font Awesome if not present
    if (!document.querySelector('link[href*="font-awesome"]')) {
        const faLink = document.createElement('link');
        faLink.rel = 'stylesheet';
        faLink.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
        document.head.appendChild(faLink);
    }
    
    // Inject widget into page
    const container = document.createElement('div');
    container.innerHTML = widgetHTML;
    document.body.appendChild(container);
    
    // Add widget styles
    const style = document.createElement('style');
    style.textContent = `
        #techcadd-chat-button:hover {
            transform: scale(1.1);
            transition: transform 0.3s;
        }
        @media (max-width: 480px) {
            #techcadd-chat-window {
                width: 90vw !important;
                right: 5vw !important;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Toggle chat window
    document.getElementById('techcadd-chat-button').addEventListener('click', function() {
        const chatWindow = document.getElementById('techcadd-chat-window');
        if (chatWindow.style.display === 'none' || !chatWindow.style.display) {
            chatWindow.style.display = 'flex';
        } else {
            chatWindow.style.display = 'none';
        }
    });
})();