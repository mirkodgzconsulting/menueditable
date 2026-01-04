document.addEventListener('DOMContentLoaded', () => {

    // ELEMENTS
    const toggleBtn = document.getElementById('modeToggle');
    const modal = document.getElementById('premiumModal');
    const closeModalBtn = document.querySelector('.close-modal');
    const body = document.body;

    let isEditing = false;

    // 1. TOGGLE MODE
    toggleBtn.addEventListener('click', () => {
        isEditing = !isEditing;

        if (isEditing) {
            body.classList.add('editing-mode');
            toggleBtn.textContent = "Modo: EDICIÓN (Activo)";
            toggleBtn.classList.remove('btn-secondary');
            toggleBtn.classList.add('active');

            // Enable editing on prices
            document.querySelectorAll('.editable').forEach(el => {
                el.setAttribute('contenteditable', 'true');
            });

        } else {
            body.classList.remove('editing-mode');
            toggleBtn.textContent = "Modo: Lectura";
            toggleBtn.classList.remove('active');
            toggleBtn.classList.add('btn-secondary');

            // Disable editing
            document.querySelectorAll('.editable').forEach(el => {
                el.removeAttribute('contenteditable');
            });
        }
    });

    // 2. INTERCEPT CLICKS ON PROTECTED ITEMS
    document.addEventListener('click', (e) => {
        if (!isEditing) return;

        // Check if clicked element or parent has 'data-protected="true"'
        const protectedTarget = e.target.closest('[data-protected="true"]');

        if (protectedTarget) {
            e.preventDefault();
            e.stopPropagation();
            showModal();
        }
    });

    // 3. MODAL LOGIC
    function showModal() {
        modal.classList.add('visible');
    }

    function hideModal() {
        modal.classList.remove('visible');
    }

    closeModalBtn.addEventListener('click', hideModal);

    // Close on click outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            hideModal();
        }
    });

});
