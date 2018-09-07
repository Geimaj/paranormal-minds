var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat')

gulp.task('styles', function(){
    gulp.src('src/styles/**/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(gulp.dest('./static/css/'))
})

//Watch task
gulp.task('watch',function() {
    gulp.watch('src/styles/**/*.scss',['styles']);
});