var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat')
var imagein = require('gulp-imagemin')
var notify = require('gulp-notify')

gulp.task('styles', function(){
    gulp.src('src/styles/**/*.scss')
        .pipe(sass({
            })
            .on('error', sass.logError))
        .pipe(concat('style.css'))
        .pipe(gulp.dest('./static/css/'))
})

//Watch task
gulp.task('watch',function() {
    gulp.watch('src/styles/**/*.scss',['styles']);
});

gulp.task('images', function(){
    return gulp.src('src/assets/**/*')
        .pipe(imagein({ optimizationLevel: 3, progressive: true, interlaced: true })
        .pipe(gulp.dest('./static/img/')))
        .pipe(notify({ message: 'Images task complete' }));
});