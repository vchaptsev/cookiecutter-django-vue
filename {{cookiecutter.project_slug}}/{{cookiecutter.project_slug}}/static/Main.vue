<template lang="html">
    <div>
        <router-view></router-view>
        {% if cookiecutter.use_progressbar == 'y' -%}<vue-progress-bar></vue-progress-bar>{% endif -%}
    </div>
</template>

<script>
export default {
    name: 'Main'
}
</script>

<style lang="scss"></style>
