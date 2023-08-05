import { createApp } from "vue";
import App from "./App.vue";

// 引入antd
import Antd from "ant-design-vue";
// 引入Vue Router

import router from "./router/index";

// const router = createRouter({
//   history: createWebHistory(),
//   routes,
// });
router.beforeEach((to, from, next) => {
  const breadcrumb = [];

  // 遍历当前路由及其父路由，获取面包屑信息
  to.matched.forEach(route => {
    if (route.meta && route.meta.breadcrumb) {
      breadcrumb.push(...route.meta.breadcrumb);
    }
  });

  // 将面包屑信息存储在路由元数据中
  to.meta.breadcrumb = breadcrumb;

  next();
});

// createApp(App).mount('#app')
const app = createApp(App);
app.use(Antd);
app.use(router);

app.mount("#app");
