document.addEventListener('DOMContentLoaded', function() {
    // AI助理弹窗控制
    const aiButton = document.querySelector('.ai-assistant');
    const aiModal = document.getElementById('aiModal');
    const modalOverlay = document.getElementById('modalOverlay');
    const aiModalContent = document.querySelector('.ai-modal-content');

    aiButton.addEventListener('click', function() {
        aiModal.classList.add('active');
    });

    // 点击遮罩层关闭弹窗
    modalOverlay.addEventListener('click', function(e) {
        // 确保点击的是遮罩层本身，而不是其子元素
        if (e.target === modalOverlay) {
            aiModal.classList.remove('active');
        }
    });

    // 按ESC键关闭弹窗
    document.addEventListener('keydown', function(e) {
        if (e.key === "Escape" && aiModal.classList.contains('active')) {
            aiModal.classList.remove('active');
        }
    });

    // 阻止弹窗内容区域的点击事件冒泡
    aiModalContent.addEventListener('click', function(e) {
        e.stopPropagation();
    });

    // 按ESC键关闭弹窗
    document.addEventListener('keydown', function(e) {
        if (e.key === "Escape" && aiModal.classList.contains('active')) {
            aiModal.classList.remove('active');
        }
    });

    // 添加问题按钮点击事件
    const addIssueBtn = document.getElementById('addIssueBtn');
    addIssueBtn.addEventListener('click', function() {
        // 获取当前被审计单位
        const auditedUnit = document.getElementById('auditedUnit').value || '未选择';

        // 创建新问题数据
        const newIssue = {
            audit_id: Math.floor(Math.random() * 1000).toString().padStart(3, '0'),
            conclusion: '新审计问题',
            process: '待填写',
            amount: Math.floor(Math.random() * 100),
            quantity: 1
        };

        // 创建新行
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${newIssue.audit_id}</td>
            <td>${newIssue.conclusion}</td>
            <td>${newIssue.process}</td>
            <td>${newIssue.amount}万</td>
            <td>${newIssue.quantity}</td>
            <td>待填写</td>
            <td class="actions">
                <button class="action-btn edit-btn" data-id="${newIssue.audit_id}" data-company="${auditedUnit}" data-conclusion="${newIssue.conclusion}">
                    <i class="fas fa-edit"></i>
                </button>
                <span class="action-divider">|</span>
                <button class="action-btn delete-btn" data-id="${newIssue.audit_id}">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        `;

        // 添加到表格
        issuesTableBody.appendChild(row);

        // 绑定编辑按钮事件
        row.querySelector('.edit-btn').addEventListener('click', function() {
            const issueId = this.getAttribute('data-id');
            openEditIssueModal(issueId);
        });

        // 绑定删除按钮事件
        document.querySelectorAll('.delete-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation(); // 阻止事件冒泡
                const issueId = this.getAttribute('data-id');
                openDeleteModal(issueId);
            });
        });
        // row.querySelector('.delete-btn').addEventListener('click', function() {
        //     const issueId = this.getAttribute('data-id');
        //     openDeleteModal(issueId);
        // });

        // 显示表格，隐藏占位符
        issuesTable.style.display = 'table';
        issuesTablePlaceholder.style.display = 'none';

        // 显示通知
        showNotification('已添加新审计问题');
    });

    // 关闭AI助手弹窗时触发API调用
    modalOverlay.addEventListener('click', function(e) {
        if (e.target === modalOverlay) {
            fetchDraftDataAndBind();
            fetchAuditDataAndBind();
            aiModal.classList.remove('active');
        }
    });

    // 按ESC键关闭弹窗时也触发API调用
    document.addEventListener('keydown', function(e) {
        if (e.key === "Escape" && aiModal.classList.contains('active')) {
            fetchDraftDataAndBind();
            fetchAuditDataAndBind();
            aiModal.classList.remove('active');
        }
    });

    // 获取底稿数据并绑定到表单的函数
    function fetchDraftDataAndBind() {
        // 显示加载状态
        showNotification('正在获取AI建议的底稿数据...');

        // 调用API获取数据
        fetch('http://127.0.0.1:5001/api/draft/query')
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应错误');
                }
                return response.json();
            })
            .then(data => {
                // 绑定数据到表单
                bindDraftDataToForm(data);
                showNotification('AI建议的底稿数据已加载');
            })
            .catch(error => {
                console.error('获取底稿数据失败:', error);
                showNotification('获取底稿数据失败', true);
            });
    }

    // 获取底稿数据并绑定到表单的函数
    function fetchAuditDataAndBind() {
        // 显示加载状态
        showNotification('正在获取AI建议的底稿数据...');

        // 调用API获取数据
        fetch('http://127.0.0.1:5001/api/audit/query')
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应错误');
                }
                return response.json();
            })
            .then(data => {
                // 绑定数据到表单
                bindAuditDataToForm(data);
                showNotification('AI建议的底稿数据已加载');
            })
            .catch(error => {
                console.error('获取底稿数据失败:', error);
                showNotification('获取底稿数据失败', true);
            });
    }

    // 将API返回的数据绑定到表单
    function bindDraftDataToForm(data) {
        // 绑定必填字段
        document.getElementById('auditItem').value = data.matter || '';
        document.getElementById('draftName').value = data.name || '';
        document.getElementById('status').value = data.status || '';
        document.getElementById('operator').value = data.operator || '';
        document.getElementById('createDate').value = data.create_date || '';
        document.getElementById('modifyDate').value = data.update_date || '';
        document.getElementById('source').value = data.source || '';
        document.getElementById('model').value = data.model || '';
        document.getElementById('draftCode').value = data.code || '';
        document.getElementById('focus').value = data.focus || '';
        document.getElementById('company_name').value = data.company_name || '';
    }

    // 将API返回的数据绑定到表单
    function bindAuditDataToForm(data) {
        document.getElementById('auditProcess').value = data.process || '';
        document.getElementById('auditConclusion').value = data.conclusion || '';

        // 清空现有表格内容
        const issuesTableBody = document.getElementById('issuesTableBody');
        issuesTableBody.innerHTML = '';

        // 检查是否有客户数据
        if (data.customer && Array.isArray(data.customer)) {
            // 遍历客户数组并添加到表格
            data.customer.forEach(customer => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${customer.customer_name || '未知'}</td>
                    <td>${customer.title || '未命名问题'}</td>
                    <td>${customer.level || '未知风险'}</td>
                    <td>${customer.amount ? customer.amount + '万' : '未知'}</td>
                    <td>${customer.quantity || '1'}</td>
                    <td>${customer.discoverer || 'AI助手'}</td>
                    <td class="actions">
                        <button class="action-btn edit-btn" data-id="${customer.detail_id}" data-company="${customer.company || '未指定'}" data-conclusion="${customer.title || ''}">
                            <i class="fas fa-edit"></i>
                        </button>
                        <span class="action-divider">|</span>
                        <button class="action-btn delete-btn" data-id="${customer.detail_id}">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                `;

                issuesTableBody.appendChild(row);

                // 绑定编辑按钮事件
                row.querySelector('.edit-btn').addEventListener('click', function() {
                    const issueId = this.getAttribute('data-id');
                    openEditIssueModal(issueId,);
                });

                // 绑定删除按钮事件
                row.querySelector('.delete-btn').addEventListener('click', function(e) {
                    e.stopPropagation();
                    const issueId = this.getAttribute('data-id');
                    openDeleteModal(issueId);
                });
            });

            // 显示表格
            document.getElementById('issuesTable').style.display = 'table';
        } else {
            // 如果没有客户数据，可以显示一条消息或保持表格为空
            console.log('没有客户数据可显示');
        }
    }

    // 保留原有的关闭弹窗事件（确保不冲突）
    aiModalContent.addEventListener('click', function(e) {
        e.stopPropagation();
    });

    // 打开删除确认弹窗
    function openDeleteModal(issueId) {
        const deleteModal = document.getElementById('deleteModal');
        const cancelDelete = document.getElementById('cancelDelete');
        const confirmDelete = document.getElementById('confirmDelete');

        // 设置删除确认按钮的回调
        confirmDelete.onclick = function() {
            // 从DOM中移除对应的行
            const rowToDelete = document.querySelector(`.delete-btn[data-id="${issueId}"]`).closest('tr');
            if (rowToDelete) {
                rowToDelete.remove();
                showNotification(`已删除问题: ${issueId}`);

                // 如果删除后表格为空，显示占位符
                if (issuesTableBody.children.length === 0) {
                    issuesTable.style.display = 'none';
                    issuesTablePlaceholder.style.display = 'flex';
                }
            }

            deleteModal.classList.remove('active');
        };

        // 取消删除按钮
        cancelDelete.onclick = function() {
            deleteModal.classList.remove('active');
        };

        deleteModal.classList.add('active');
    }

    function openEditIssueModal(issueId) {
        const editModal = document.getElementById('editIssueModal');
        const closeEditModal = document.getElementById('closeEditModal');

        // 显示加载状态
        showLoadingInModal(true);

        console.log(issueId)

        // 请求接口数据
        fetch(`http://127.0.0.1:5001/api/audit/query/by_detail_id?detail_id=${issueId}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应错误');
                }
                return response.json();
            })
            .then(data => {
                // 填充数据到弹窗
                populateEditModal(data);
                showLoadingInModal(false);
                editModal.classList.add('active');
            })
            .catch(error => {
                console.error('获取审计问题详情失败:', error);
                showNotification('获取问题详情失败', true);
                showLoadingInModal(false);
            });

        // 关闭弹窗按钮事件
        closeEditModal.onclick = function() {
            editModal.classList.remove('active');
        };
    }

    // 在弹窗中显示加载状态
    function showLoadingInModal(show) {
        const loading = document.getElementById('editModalLoading');
        const content = document.getElementById('editModalContent');

        if (show) {
            loading.style.display = 'flex';
            content.style.display = 'none';
        } else {
            loading.style.display = 'none';
            content.style.display = 'block';
        }
    }

    // 填充数据到编辑弹窗
    function populateEditModal(data) {
        // 基本信息
        document.getElementById('editCustomerName').value = data.customer_name || companyName;
        document.getElementById('editIssueTitle').value = data.title || '';
        document.getElementById('editIssueLevel').value = data.level || '';
        document.getElementById('editIssueDesc').value = data.desc || '';
        document.getElementById('editIssueSuggest').value = data.suggest || '';

        // 附件列表
        const attachmentsTableBody = document.getElementById('attachmentsTableBody');
        attachmentsTableBody.innerHTML = '';

        if (data.attach && data.attach.length > 0) {
            data.attach.forEach(attachment => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${attachment.name}</td>
                    <td>${formatFileSize(attachment.filesize)}</td>
                    <td>${formatDateTime(attachment.dateTime)}</td>
                    <td>
                        <button class="file-action-btn download" data-url="${attachment.url}">
                            <i class="fas fa-download"></i> 下载
                        </button>
                    </td>
                `;
                attachmentsTableBody.appendChild(row);

                // 绑定下载按钮事件
                row.querySelector('.download').addEventListener('click', function() {
                    window.open(this.getAttribute('data-url'), '_blank');
                });
            });
        } else {
            attachmentsTableBody.innerHTML = `
                <tr>
                    <td colspan="4" style="text-align: center; color: var(--gray);">
                        暂无附件
                    </td>
                </tr>
            `;
        }
    }

    // 格式化文件大小
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    // 格式化日期时间
    function formatDateTime(dateTimeString) {
        const date = new Date(dateTimeString);
        return date.toLocaleString('zh-CN', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    // 显示通知
    function showNotification(message, isError = false) {
        const notification = document.createElement('div');
        notification.textContent = message;
        notification.style.position = 'fixed';
        notification.style.bottom = '20px';
        notification.style.right = '20px';
        notification.style.backgroundColor = isError ? 'var(--error)' : 'var(--primary)';
        notification.style.color = 'white';
        notification.style.padding = '10px 20px';
        notification.style.borderRadius = '5px';
        notification.style.zIndex = '3000';
        notification.style.boxShadow = '0 3px 10px rgba(0,0,0,0.2)';
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
});