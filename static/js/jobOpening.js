$(document).ready(function () {

    // Lấy các phần tử modal và các nút
    const modal = $('#modal')
    const openModal = $('#open-modal')
    const closeModal = $('#close-modal')

    function isMobileDevice() {
        return /Mobi|Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    }

    // Sự kiện mở modal
    openModal.on('click', function () {

        let checkDevice = "desktop"

        if (isMobileDevice()) {
            checkDevice = "mobile"
        }

        if (checkDevice === "mobile") {

            toastr.error("Vui lòng sử dụng máy tính để ứng tuyển...!")
            return;
        }
        modal.removeClass('hidden')
    })

    closeModal.on('click', function () {
        modal.addClass('hidden')
    })

    // Sự kiện thay đổi file input
    $('#CV').on('change', function (event) {
        // Lấy tên file từ input
        const fileName = event.target.files[0].name;

        // Tìm div để hiển thị tên file
        const displayDiv = $('#file-name-display');

        // Kiểm tra nếu có tên file, hiển thị nó thay vì icon
        if (fileName) {
            displayDiv.html(`<span class="text-main">${fileName}</span>`);
        }
    });
})