function refresh_description()
{
	var topic_id = $('#id_topic').val();
	if (topic_id == '')
	{
		$('#topic_desc').hide();
		$('#mediainfo-group').hide();
		$('#expediture-group').hide();
		$('#preexpediture-group').hide();
		$('.field_car_travel').hide();
		return;
	}

	var topic = topics_table[topic_id];

	$('#topic_desc').html(topic['form_description']).toggle(topic['form_description'] != "");
	$('#mediainfo-group').toggle(topic['ticket_media']);
	$('#expediture-group').toggle(topic['ticket_expenses']);
	$('#preexpediture-group').toggle(topic['ticket_preexpenses']);
	$('.field_car_travel').toggle(topic['ticket_statutory_declaration']);
}

$(document).ready(function() {
	$('#id_topic').change(refresh_description);
	refresh_description();
});
