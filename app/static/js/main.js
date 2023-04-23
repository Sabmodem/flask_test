async function delete_appointment(id) {
  const delete_options = { method: 'DELETE' };
  try {
    await fetch(`/appointment/${id}`, delete_options);
    window.location.reload();
  } catch(err) {
    alert('Ошибка удаления');
  }
}