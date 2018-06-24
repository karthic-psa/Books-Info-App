module.exports = function(grunt) {
    grunt.initConfig({
        image_resize: {
            resize: {
                options: {
                    width: 300,
                    height: 470
                },
            //     files: {
            //         'static/images/test.jpg': 'static/images_src/bookshero.jpg'
            // }
                  src: 'static/images_src/*.jpg',
                dest: 'static/images/'
        }
    }})
    grunt.loadNpmTasks('grunt-image-resize');
    grunt.registerTask('default', ['image_resize']);
};